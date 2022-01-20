# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

"""
This module implements equivalents of the basic ComputedEntry objects, which
is the basic entity that can be used to perform many analyses. ComputedEntries
contain calculated information, typically from VASP or other electronic
structure codes. For example, ComputedEntries can be used as inputs for phase
diagram analysis.
"""

import abc
import json
import os
import warnings
from itertools import combinations
from typing import Dict, List, Literal, Union

import numpy as np
from monty.json import MontyDecoder, MontyEncoder, MSONable
from scipy.interpolate import interp1d
from uncertainties import ufloat

from pymatgen.core.composition import Composition
from pymatgen.core.structure import Structure
from pymatgen.entries import Entry

__author__ = "Ryan Kingsbury, Matt McDermott, Shyue Ping Ong, Anubhav Jain"
__copyright__ = "Copyright 2011-2020, The Materials Project"
__version__ = "1.1"
__date__ = "April 2020"

with open(os.path.join(os.path.dirname(__file__), "data/g_els.json")) as f:
    G_ELEMS = json.load(f)
with open(os.path.join(os.path.dirname(__file__), "data/nist_gas_gf.json")) as f:
    G_GASES = json.load(f)


class EnergyAdjustment(MSONable):
    """
    Lightweight class to contain information about an energy adjustment or
    energy correction.
    """

    def __init__(
        self,
        value,
        uncertainty=np.nan,
        name="Manual adjustment",
        cls=None,
        description="",
    ):
        """
        Args:
            value: float, value of the energy adjustment in eV
            uncertainty: float, uncertainty of the energy adjustment in eV. Default: np.nan
            name: str, human-readable name of the energy adjustment.
                (Default: Manual adjustment)
            cls: dict, Serialized Compatibility class used to generate the energy adjustment. (Default: None)
            description: str, human-readable explanation of the energy adjustment.
        """
        self.name = name
        self.cls = cls if cls else {}
        self.description = description
        self._value = value
        self._uncertainty = uncertainty

    @property
    def value(self):
        """
        Return the value of the energy correction in eV.
        """
        return self._value

    @property
    def uncertainty(self):
        """
        Return the uncertainty in the value of the energy adjustment in eV
        """
        return self._uncertainty

    @abc.abstractmethod
    def normalize(self, factor):
        """
        Scale the value of the current energy adjustment by factor in-place.

        This method is utilized in ComputedEntry.normalize() to scale the energies to a formula unit basis
        (e.g. E_Fe6O9 = 3 x E_Fe2O3).
        """

    @property
    @abc.abstractmethod
    def explain(self):
        """
        Return an explanaion of how the energy adjustment is calculated.
        """

    def __repr__(self):
        output = [
            f"{self.__class__.__name__}:",
            f"  Name: {self.name}",
            f"  Value: {self.value:.3f} eV",
            f"  Uncertainty: {self.uncertainty:.3f} eV",
            f"  Description: {self.explain}",
            "  Generated by: {}".format(self.cls.get("@class", None)),
        ]
        return "\n".join(output)


class ConstantEnergyAdjustment(EnergyAdjustment):
    """
    A constant energy adjustment applied to a ComputedEntry. Useful in energy referencing
    schemes such as the Aqueous energy referencing scheme.
    """

    def __init__(
        self,
        value,
        uncertainty=np.nan,
        name="Constant energy adjustment",
        cls=None,
        description="Constant energy adjustment",
    ):
        """
        Args:
            value: float, value of the energy adjustment in eV
            uncertainty: float, uncertaint of the energy adjustment in eV. (Default: np.nan)
            name: str, human-readable name of the energy adjustment.
                (Default: Constant energy adjustment)
            cls: dict, Serialized Compatibility class used to generate the energy
                adjustment. (Default: None)
            description: str, human-readable explanation of the energy adjustment.
        """
        super().__init__(value, uncertainty, name=name, cls=cls, description=description)
        self._value = value
        self._uncertainty = uncertainty

    @property
    def explain(self):
        """
        Return an explanaion of how the energy adjustment is calculated.
        """
        return self.description + f" ({self.value:.3f} eV)"

    def normalize(self, factor):
        """
        Normalize energy adjustment (in place), dividing value/uncertainty by a
        factor.
        :param factor: factor to divide by
        """
        self._value /= factor
        self._uncertainty /= factor


class ManualEnergyAdjustment(ConstantEnergyAdjustment):
    """
    A manual energy adjustment applied to a ComputedEntry.
    """

    def __init__(self, value):
        """
        Args:
            value: float, value of the energy adjustment in eV
        """
        name = "Manual energy adjustment"
        description = "Manual energy adjustment"
        super().__init__(value, name=name, cls=None, description=description)


class CompositionEnergyAdjustment(EnergyAdjustment):
    """
    An energy adjustment applied to a ComputedEntry based on the atomic composition.
    Used in various DFT energy correction schemes.
    """

    def __init__(
        self,
        adj_per_atom,
        n_atoms,
        uncertainty_per_atom=np.nan,
        name="",
        cls=None,
        description="Composition-based energy adjustment",
    ):
        """
        Args:
            adj_per_atom: float, energy adjustment to apply per atom, in eV/atom
            n_atoms: float or int, number of atoms.
            uncertainty_per_atom: float, uncertainty in energy adjustment to apply per atom, in eV/atom.
                (Default: np.nan)
            name: str, human-readable name of the energy adjustment.
                (Default: "")
            cls: dict, Serialized Compatibility class used to generate the energy
                adjustment. (Default: None)
            description: str, human-readable explanation of the energy adjustment.
        """
        self._adj_per_atom = adj_per_atom
        self.uncertainty_per_atom = uncertainty_per_atom
        self.n_atoms = n_atoms
        self.cls = cls if cls else {}
        self.name = name
        self.description = description

    @property
    def value(self):
        """
        Return the value of the energy adjustment in eV.
        """
        return self._adj_per_atom * self.n_atoms

    @property
    def uncertainty(self):
        """
        Return the value of the energy adjustment in eV.
        """
        return self.uncertainty_per_atom * self.n_atoms

    @property
    def explain(self):
        """
        Return an explanaion of how the energy adjustment is calculated.
        """
        return self.description + f" ({self._adj_per_atom:.3f} eV/atom x {self.n_atoms} atoms)"

    def normalize(self, factor):
        """
        Normalize energy adjustment (in place), dividing value/uncertainty by a
        factor.
        :param factor: factor to divide by
        """
        self.n_atoms /= factor


class TemperatureEnergyAdjustment(EnergyAdjustment):
    """
    An energy adjustment applied to a ComputedEntry based on the temperature.
    Used, for example, to add entropy to DFT energies.
    """

    def __init__(
        self,
        adj_per_deg,
        temp,
        n_atoms,
        uncertainty_per_deg=np.nan,
        name="",
        cls=None,
        description="Temperature-based energy adjustment",
    ):
        """
        Args:
            adj_per_deg: float, energy adjustment to apply per degree K, in eV/atom
            temp: float, temperature in Kelvin
            n_atoms: float or int, number of atoms
            uncertainty_per_deg: float, uncertainty in energy adjustment to apply per degree K,
                in eV/atom. (Default: np.nan)
            name: str, human-readable name of the energy adjustment.
                (Default: "")
            cls: dict, Serialized Compatibility class used to generate the energy
                adjustment. (Default: None)
            description: str, human-readable explanation of the energy adjustment.
        """
        self._adj_per_deg = adj_per_deg
        self.uncertainty_per_deg = uncertainty_per_deg
        self.temp = temp
        self.n_atoms = n_atoms
        self.name = name
        self.cls = cls if cls else {}
        self.description = description

    @property
    def value(self):
        """
        Return the value of the energy correction in eV.
        """
        return self._adj_per_deg * self.temp * self.n_atoms

    @property
    def uncertainty(self):
        """
        Return the value of the energy adjustment in eV.
        """
        return self.uncertainty_per_deg * self.temp * self.n_atoms

    @property
    def explain(self):
        """
        Return an explanaion of how the energy adjustment is calculated.
        """
        return self.description + " ({:.4f} eV/K/atom x {} K x {} atoms)".format(
            self._adj_per_deg, self.temp, self.n_atoms
        )

    def normalize(self, factor):
        """
        Normalize energy adjustment (in place), dividing value/uncertainty by a
        factor.
        :param factor: factor to divide by
        """
        self.n_atoms /= factor


class ComputedEntry(Entry):
    """
    Lightweight Entry object for computed data. Contains facilities
    for applying corrections to the energy attribute and for storing
    calculation parameters.
    """

    def __init__(
        self,
        composition: Union[Composition, str, Dict[str, float]],
        energy: float,
        correction: float = 0.0,
        energy_adjustments: list = None,
        parameters: dict = None,
        data: dict = None,
        entry_id: object = None,
    ):
        """
        Initializes a ComputedEntry.

        Args:
            composition (Composition): Composition of the entry. For
                flexibility, this can take the form of all the typical input
                taken by a Composition, including a {symbol: amt} dict,
                a string formula, and others.
            energy (float): Energy of the entry. Usually the final calculated
                energy from VASP or other electronic structure codes.
            correction (float): Manually set an energy correction, will ignore
                energy_adjustments if specified.
            energy_adjustments: An optional list of EnergyAdjustment to
                be applied to the energy. This is used to modify the energy for
                certain analyses. Defaults to None.
            parameters: An optional dict of parameters associated with
                the entry. Defaults to None.
            data: An optional dict of any additional data associated
                with the entry. Defaults to None.
            entry_id: An optional id to uniquely identify the entry.
        """
        super().__init__(composition, energy)
        self.energy_adjustments = energy_adjustments if energy_adjustments else []

        if correction != 0.0:
            if energy_adjustments:
                raise ValueError(
                    "Argument conflict! Setting correction = {:.3f} conflicts "
                    "with setting energy_adjustments. Specify one or the "
                    "other.".format(correction)
                )

            self.correction = correction

        self.parameters = parameters if parameters else {}
        self.data = data if data else {}
        self.entry_id = entry_id
        self.name = self.composition.reduced_formula

    @property
    def uncorrected_energy(self) -> float:
        """
        Returns:
            float: the *uncorrected* energy of the entry
        """
        return self._energy

    @property
    def energy(self) -> float:
        """
        :return: the *corrected* energy of the entry.
        """
        return self.uncorrected_energy + self.correction

    @property
    def uncorrected_energy_per_atom(self) -> float:
        """
        Returns:
            float: the *uncorrected* energy of the entry, normalized by atoms
                (units of eV/atom)
        """
        return self.uncorrected_energy / self.composition.num_atoms

    @property
    def correction(self) -> float:
        """
        Returns:
            float: the total energy correction / adjustment applied to the entry,
                in eV.
        """
        # adds to ufloat(0.0, 0.0) to ensure that no corrections still result in ufloat object
        corr = ufloat(0.0, 0.0) + sum(ufloat(ea.value, ea.uncertainty) for ea in self.energy_adjustments)
        return corr.nominal_value

    @correction.setter
    def correction(self, x: float) -> None:
        corr = ManualEnergyAdjustment(x)
        self.energy_adjustments = [corr]

    @property
    def correction_per_atom(self) -> float:
        """
        Returns:
            float: the total energy correction / adjustment applied to the entry,
                normalized by atoms (units of eV/atom)
        """
        return self.correction / self.composition.num_atoms

    @property
    def correction_uncertainty(self) -> float:
        """
        Returns:
            float: the uncertainty of the energy adjustments applied to the entry, in eV
        """
        # adds to ufloat(0.0, 0.0) to ensure that no corrections still result in ufloat object
        unc = ufloat(0.0, 0.0) + sum(
            ufloat(ea.value, ea.uncertainty) if not np.isnan(ea.uncertainty) else ufloat(ea.value, 0)
            for ea in self.energy_adjustments
        )

        if unc.nominal_value != 0 and unc.std_dev == 0:
            return np.nan

        return unc.std_dev

    @property
    def correction_uncertainty_per_atom(self) -> float:
        """
        Returns:
            float: the uncertainty of the energy adjustments applied to the entry,
                normalized by atoms (units of eV/atom)
        """
        return self.correction_uncertainty / self.composition.num_atoms

    def normalize(self, mode: Literal["formula_unit", "atom"] = "formula_unit") -> "ComputedEntry":
        """
        Normalize the entry's composition and energy.

        Args:
            mode ("formula_unit" | "atom"): "formula_unit" (the default) normalizes to composition.reduced_formula.
                "atom" normalizes such that the composition amounts sum to 1.
        """

        factor = self._normalization_factor(mode)
        new_composition = self._composition / factor
        new_energy = self._energy / factor

        new_entry_dict = self.as_dict()
        new_entry_dict["composition"] = new_composition.as_dict()
        new_entry_dict["energy"] = new_energy

        # TODO: make sure EnergyAdjustments are _also_ immutable to avoid this hacking
        new_energy_adjustments = MontyDecoder().process_decoded(new_entry_dict["energy_adjustments"])
        for ea in new_energy_adjustments:
            ea.normalize(factor)
        new_entry_dict["energy_adjustments"] = [ea.as_dict() for ea in new_energy_adjustments]

        return self.from_dict(new_entry_dict)

    def __repr__(self) -> str:
        n_atoms = self.composition.num_atoms
        output = [
            "{} {:<10} - {:<12} ({})".format(
                self.entry_id,
                self.__class__.__name__,
                self.composition.formula,
                self.composition.reduced_formula,
            ),
            "{:<24} = {:<9.4f} eV ({:<8.4f} eV/atom)".format(
                "Energy (Uncorrected)", self._energy, self._energy / n_atoms
            ),
            "{:<24} = {:<9.4f} eV ({:<8.4f} eV/atom)".format("Correction", self.correction, self.correction / n_atoms),
            "{:<24} = {:<9.4f} eV ({:<8.4f} eV/atom)".format("Energy (Final)", self.energy, self.energy_per_atom),
            "Energy Adjustments:",
        ]
        if len(self.energy_adjustments) == 0:
            output.append("  None")
        else:
            for e in self.energy_adjustments:
                output.append(f"  {e.name:<23}: {e.value:<9.4f} eV ({e.value / n_atoms:<8.4f} eV/atom)")
        output.append("Parameters:")
        for k, v in self.parameters.items():
            output.append(f"  {k:<22} = {v}")
        output.append("Data:")
        for k, v in self.data.items():
            output.append(f"  {k:<22} = {v}")
        return "\n".join(output)

    def __str__(self):
        return self.__repr__()

    def __eq__(self, other):
        # NOTE: Scaled duplicates i.e. physically equivalent materials
        # are not equal unless normalized separately.
        if self is other:
            return True

        # Equality is defined based on composition and energy
        # If structures are involved, it is assumed that a {composition, energy} is
        # vanishingly unlikely to be the same if the structures are different
        # if entry_ids are equivalent, skip the more expensive composition check

        if getattr(self, "entry_id", None) and getattr(other, "entry_id", None):
            return self.entry_id == other.entry_id

        if not np.allclose(self.energy, other.energy):
            return False

        if self.composition != other.composition:
            return False

        # assumes that data, parameters, corrections are equivalent
        return True

    @classmethod
    def from_dict(cls, d) -> "ComputedEntry":
        """
        :param d: Dict representation.
        :return: ComputedEntry
        """
        dec = MontyDecoder()
        # the first block here is for legacy ComputedEntry that were
        # serialized before we had the energy_adjustments attribute.
        if d["correction"] != 0 and not d.get("energy_adjustments"):
            return cls(
                d["composition"],
                d["energy"],
                d["correction"],
                parameters={k: dec.process_decoded(v) for k, v in d.get("parameters", {}).items()},
                data={k: dec.process_decoded(v) for k, v in d.get("data", {}).items()},
                entry_id=d.get("entry_id", None),
            )
        # this is the preferred / modern way of instantiating ComputedEntry
        # we don't pass correction explicitly because it will be calculated
        # on the fly from energy_adjustments
        return cls(
            d["composition"],
            d["energy"],
            correction=0,
            energy_adjustments=[dec.process_decoded(e) for e in d.get("energy_adjustments", {})],
            parameters={k: dec.process_decoded(v) for k, v in d.get("parameters", {}).items()},
            data={k: dec.process_decoded(v) for k, v in d.get("data", {}).items()},
            entry_id=d.get("entry_id", None),
        )

    def as_dict(self) -> dict:
        """
        :return: MSONable dict.
        """
        return_dict = super().as_dict()
        return_dict.update(
            {
                "entry_id": self.entry_id,
                "correction": self.correction,
                "energy_adjustments": json.loads(json.dumps(self.energy_adjustments, cls=MontyEncoder)),
                "parameters": json.loads(json.dumps(self.parameters, cls=MontyEncoder)),
                "data": json.loads(json.dumps(self.data, cls=MontyEncoder)),
            }
        )
        return return_dict

    def __hash__(self) -> int:
        # NOTE It is assumed that the user will ensure entry_id is a
        # unique identifier for ComputedEntry type classes.
        if self.entry_id is not None:
            return hash(f"{self.__class__.__name__}{self.entry_id}")

        return super().__hash__()


class ComputedStructureEntry(ComputedEntry):
    """
    A heavier version of ComputedEntry which contains a structure as well. The
    structure is needed for some analyses.
    """

    def __init__(
        self,
        structure: Structure,
        energy: float,
        correction: float = 0.0,
        composition: Union[Composition, str, Dict[str, float]] = None,
        energy_adjustments: list = None,
        parameters: dict = None,
        data: dict = None,
        entry_id: object = None,
    ):
        """
        Initializes a ComputedStructureEntry.

        Args:
            structure (Structure): The actual structure of an entry.
            energy (float): Energy of the entry. Usually the final calculated
                energy from VASP or other electronic structure codes.
            energy_adjustments: An optional list of EnergyAdjustment to
                be applied to the energy. This is used to modify the energy for
                certain analyses. Defaults to None.
            composition (Composition): Composition of the entry. For
                flexibility, this can take the form of all the typical input
                taken by a Composition, including a {symbol: amt} dict,
                a string formula, and others.
            parameters: An optional dict of parameters associated with
                the entry. Defaults to None.
            data: An optional dict of any additional data associated
                with the entry. Defaults to None.
            entry_id: An optional id to uniquely identify the entry.
        """

        if composition:
            composition = Composition(composition)
            if (
                composition.get_integer_formula_and_factor()[0]
                != structure.composition.get_integer_formula_and_factor()[0]
            ):
                raise ValueError("Mismatching composition provided.")
        else:
            composition = structure.composition

        super().__init__(
            composition,
            energy,
            correction=correction,
            energy_adjustments=energy_adjustments,
            parameters=parameters,
            data=data,
            entry_id=entry_id,
        )
        self._structure = structure

    @property
    def structure(self) -> Structure:
        """
        :return: the structure of the entry.
        """
        return self._structure

    def as_dict(self) -> dict:
        """
        :return: MSONAble dict.
        """
        d = super().as_dict()
        d["structure"] = self.structure.as_dict()
        return d

    @classmethod
    def from_dict(cls, d) -> "ComputedStructureEntry":
        """
        :param d: Dict representation.
        :return: ComputedStructureEntry
        """
        dec = MontyDecoder()
        # the first block here is for legacy ComputedEntry that were
        # serialized before we had the energy_adjustments attribute.
        if d["correction"] != 0 and not d.get("energy_adjustments"):
            struct = dec.process_decoded(d["structure"])
            return cls(
                struct,
                d["energy"],
                correction=d["correction"],
                parameters={k: dec.process_decoded(v) for k, v in d.get("parameters", {}).items()},
                data={k: dec.process_decoded(v) for k, v in d.get("data", {}).items()},
                entry_id=d.get("entry_id", None),
            )
        # this is the preferred / modern way of instantiating ComputedEntry
        # we don't pass correction explicitly because it will be calculated
        # on the fly from energy_adjustments
        return cls(
            dec.process_decoded(d["structure"]),
            d["energy"],
            composition=d.get("composition", None),
            correction=0,
            energy_adjustments=[dec.process_decoded(e) for e in d.get("energy_adjustments", {})],
            parameters={k: dec.process_decoded(v) for k, v in d.get("parameters", {}).items()},
            data={k: dec.process_decoded(v) for k, v in d.get("data", {}).items()},
            entry_id=d.get("entry_id", None),
        )

    def normalize(self, mode: Literal["formula_unit", "atom"] = "formula_unit") -> "ComputedStructureEntry":
        """
        Normalize the entry's composition and energy. The structure remains
        unchanged.
        Args:
            mode ("formula_unit" | "atom"): "formula_unit" (the default) normalizes to composition.reduced_formula.
                "atom" normalizes such that the composition amounts sum to 1.
        """
        # TODO: this should raise TypeError since normalization does not make sense
        # raise TypeError("You cannot normalize a structure.")
        warnings.warn(
            f"Normalization of a `{self.__class__.__name__}` makes "
            "`self.composition` and `self.structure.composition` inconsistent"
            " - please use self.composition for all further calculations."
        )
        # TODO: find a better solution for creating copies instead of as/from dict
        factor = self._normalization_factor(mode)
        d = super().normalize(mode).as_dict()
        d["structure"] = self.structure.as_dict()
        entry = self.from_dict(d)
        entry._composition /= factor  # pylint: disable=E1101
        return entry


class GibbsComputedStructureEntry(ComputedStructureEntry):
    """
    An extension to ComputedStructureEntry which includes the estimated Gibbs
    free energy of formation via a machine-learned model.
    """

    def __init__(
        self,
        structure: Structure,
        formation_enthalpy_per_atom: float,
        temp: float = 300,
        gibbs_model: Literal["SISSO"] = "SISSO",
        composition: Composition = None,
        correction: float = 0.0,
        energy_adjustments: list = None,
        parameters: dict = None,
        data: dict = None,
        entry_id: object = None,
    ):
        """
        Args:
            structure (Structure): The pymatgen Structure object of an entry.
            formation_enthalpy_per_atom (float): Formation enthalpy of the entry;
            must be
                calculated using phase diagram construction (eV)
            temp (float): Temperature in Kelvin. If temperature is not selected from
                one of [300, 400, 500, ... 2000 K], then free energies will
                be interpolated. Defaults to 300 K.
            gibbs_model ('SISSO'): Model for Gibbs Free energy. "SISSO", the descriptor
                created by Bartel et al. (2018) -- see reference in documentation, is
                currently the only supported) option.
            correction (float): A correction to be applied to the energy. Defaults to 0
            parameters (dict): An optional dict of parameters associated with
                the entry. Defaults to None.
            data (dict): An optional dict of any additional data associated
                with the entry. Defaults to None.
            entry_id: An optional id to uniquely identify the entry.
        """
        if temp < 300 or temp > 2000:
            raise ValueError("Temperature must be selected from range: [300, 2000] K.")

        integer_formula, _ = structure.composition.get_integer_formula_and_factor()

        self.experimental = False
        if integer_formula in G_GASES.keys():
            self.experimental = True
            if "Experimental" not in str(entry_id):
                entry_id = f"{entry_id} (Experimental)"

        super().__init__(
            structure,
            energy=0,  # placeholder, energy reassigned at end of __init__
            composition=composition,
            correction=correction,
            energy_adjustments=energy_adjustments,
            parameters=parameters,
            data=data,
            entry_id=entry_id,
        )

        self.temp = temp
        self.gibbs_model = gibbs_model
        self.formation_enthalpy_per_atom = formation_enthalpy_per_atom

        self.interpolated = False
        if self.temp % 100:
            self.interpolated = True

        if gibbs_model.lower() == "sisso":
            self.gibbs_fn = self.gf_sisso
        else:
            raise ValueError(f"{gibbs_model} not a valid model. The only currently available model is 'SISSO'.")

        self._energy = self.gibbs_fn()

    def gf_sisso(self) -> float:
        """
        Gibbs Free Energy of formation as calculated by SISSO descriptor from Bartel
        et al. (2018). Units: eV (not normalized)

        WARNING: This descriptor only applies to solids. The implementation here
        attempts to detect and use downloaded NIST-JANAF data for common
        experimental gases (e.g. CO2) where possible. Note that experimental data is
        only for Gibbs Free Energy of formation, so expt. entries will register as
        having a formation enthalpy of 0.

        Reference: Bartel, C. J., Millican, S. L., Deml, A. M., Rumptz, J. R.,
        Tumas, W., Weimer, A. W., … Holder, A. M. (2018). Physical descriptor for
        the Gibbs energy of inorganic crystalline solids and
        temperature-dependent materials chemistry. Nature Communications, 9(1),
        4168. https://doi.org/10.1038/s41467-018-06682-4

        Returns:
            float: the difference between formation enthalpy (T=0 K, Materials
            Project) and the predicted Gibbs free energy of formation  (eV)
        """
        comp = self.composition

        if comp.is_element:
            return 0

        integer_formula, factor = comp.get_integer_formula_and_factor()
        if self.experimental:
            data = G_GASES[integer_formula]

            if self.interpolated:
                g_interp = interp1d([int(t) for t in data.keys()], list(data.values()))
                energy = g_interp(self.temp)
            else:
                energy = data[str(self.temp)]

            gibbs_energy = energy * factor
        else:
            num_atoms = self.structure.num_sites
            vol_per_atom = self.structure.volume / num_atoms
            reduced_mass = self._reduced_mass(self.structure)

            gibbs_energy = (
                comp.num_atoms
                * (self.formation_enthalpy_per_atom + self._g_delta_sisso(vol_per_atom, reduced_mass, self.temp))
                - self._sum_g_i()
            )

        return gibbs_energy

    def _sum_g_i(self) -> float:
        """
        Sum of the stoichiometrically weighted chemical potentials of the elements
        at specified temperature, as acquired from "g_els.json".

        Returns:
             float: sum of weighted chemical potentials [eV]
        """
        elems = self.composition.get_el_amt_dict()

        if self.interpolated:
            sum_g_i = 0
            for elem, amt in elems.items():
                g_interp = interp1d(
                    [float(t) for t in G_ELEMS.keys()],
                    [g_dict[elem] for g_dict in G_ELEMS.values()],
                )
                sum_g_i += amt * g_interp(self.temp)
        else:
            sum_g_i = sum(amt * G_ELEMS[str(self.temp)][elem] for elem, amt in elems.items())

        return sum_g_i

    @staticmethod
    def _reduced_mass(structure) -> float:
        """
        Reduced mass as calculated via Eq. 6 in Bartel et al. (2018)

        Args:
            structure (Structure): The pymatgen Structure object of the entry.

        Returns:
            float: reduced mass (amu)
        """
        reduced_comp = structure.composition.reduced_composition
        num_elems = len(reduced_comp.elements)
        elem_dict = reduced_comp.get_el_amt_dict()

        denominator = (num_elems - 1) * reduced_comp.num_atoms

        all_pairs = combinations(elem_dict.items(), 2)
        mass_sum = 0

        for pair in all_pairs:
            m_i = Composition(pair[0][0]).weight
            m_j = Composition(pair[1][0]).weight
            alpha_i = pair[0][1]
            alpha_j = pair[1][1]

            mass_sum += (alpha_i + alpha_j) * (m_i * m_j) / (m_i + m_j)  # type: ignore

        reduced_mass = (1 / denominator) * mass_sum

        return reduced_mass

    @staticmethod
    def _g_delta_sisso(vol_per_atom, reduced_mass, temp) -> float:
        """
        G^delta as predicted by SISSO-learned descriptor from Eq. (4) in
        Bartel et al. (2018).

        Args:
            vol_per_atom (float): volume per atom [Å^3/atom]
            reduced_mass (float) - reduced mass as calculated with pair-wise sum formula
                [amu]
            temp (float) - Temperature [K]

        Returns:
            float: G^delta [eV/atom]
        """

        return (
            (-2.48e-4 * np.log(vol_per_atom) - 8.94e-5 * reduced_mass / vol_per_atom) * temp
            + 0.181 * np.log(temp)
            - 0.882
        )

    @classmethod
    def from_pd(cls, pd, temp=300, gibbs_model="SISSO") -> List["GibbsComputedStructureEntry"]:
        """
        Constructor method for initializing a list of GibbsComputedStructureEntry
        objects from an existing T = 0 K phase diagram composed of
        ComputedStructureEntry objects, as acquired from a thermochemical database;
        (e.g.. The Materials Project)

        Args:
            pd (PhaseDiagram): T = 0 K phase diagram as created in pymatgen. Must
                contain ComputedStructureEntry objects.
            temp (int): Temperature [K] for estimating Gibbs free energy of formation.
            gibbs_model (str): Gibbs model to use; currently the only option is "SISSO".

        Returns:
            [GibbsComputedStructureEntry]: list of new entries which replace the orig.
                entries with inclusion of Gibbs free energy of formation at the
                specified temperature.
        """
        gibbs_entries = []
        for entry in pd.all_entries:
            if entry in pd.el_refs.values() or not entry.composition.is_element:
                gibbs_entries.append(
                    cls(
                        entry.structure,
                        formation_enthalpy_per_atom=pd.get_form_energy_per_atom(entry),
                        temp=temp,
                        correction=0,
                        gibbs_model=gibbs_model,
                        data=entry.data,
                        entry_id=entry.entry_id,
                    )
                )
        return gibbs_entries

    @classmethod
    def from_entries(cls, entries, temp=300, gibbs_model="SISSO") -> List["GibbsComputedStructureEntry"]:
        """
        Constructor method for initializing GibbsComputedStructureEntry objects from
        T = 0 K ComputedStructureEntry objects, as acquired from a thermochemical
        database e.g. The Materials Project.

        Args:
            entries ([ComputedStructureEntry]): List of ComputedStructureEntry objects,
                as downloaded from The Materials Project API.
            temp (int): Temperature [K] for estimating Gibbs free energy of formation.
            gibbs_model (str): Gibbs model to use; currently the only option is "SISSO".

        Returns:
            [GibbsComputedStructureEntry]: list of new entries which replace the orig.
                entries with inclusion of Gibbs free energy of formation at the
                specified temperature.
        """
        from pymatgen.analysis.phase_diagram import PhaseDiagram

        pd = PhaseDiagram(entries)
        return cls.from_pd(pd, temp, gibbs_model)

    def as_dict(self) -> dict:
        """
        :return: MSONAble dict.
        """
        d = super().as_dict()
        d["formation_enthalpy_per_atom"] = self.formation_enthalpy_per_atom
        d["temp"] = self.temp
        d["gibbs_model"] = self.gibbs_model
        d["interpolated"] = self.interpolated
        return d

    @classmethod
    def from_dict(cls, d) -> "GibbsComputedStructureEntry":
        """
        :param d: Dict representation.
        :return: GibbsComputedStructureEntry
        """
        dec = MontyDecoder()
        return cls(
            dec.process_decoded(d["structure"]),
            d["formation_enthalpy_per_atom"],
            d["temp"],
            d["gibbs_model"],
            composition=d.get("composition", None),
            correction=d["correction"],
            energy_adjustments=[dec.process_decoded(e) for e in d.get("energy_adjustments", {})],
            parameters={k: dec.process_decoded(v) for k, v in d.get("parameters", {}).items()},
            data={k: dec.process_decoded(v) for k, v in d.get("data", {}).items()},
            entry_id=d.get("entry_id", None),
        )

    def __repr__(self):
        output = [
            f"GibbsComputedStructureEntry {self.entry_id} - {self.composition.formula}",
            f"Gibbs Free Energy (Formation) = {self.energy:.4f}",
        ]
        return "\n".join(output)
