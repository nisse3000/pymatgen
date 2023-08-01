---
layout: default
title: pymatgen.io.feff.md
nav_exclude: true
---

# pymatgen.io.feff package

This package provides the modules to perform FEFF IO.

FEFF: [http://feffproject.org/feffproject-feff.html](http://feffproject.org/feffproject-feff.html)

## Subpackages


* [pymatgen.io.feff.tests package](pymatgen.io.feff.tests.md)




    * [pymatgen.io.feff.tests.test_inputs module](pymatgen.io.feff.tests.md#module-pymatgen.io.feff.tests.test_inputs)


        * [`FeffAtomsTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest)


            * [`FeffAtomsTest.setUpClass()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.setUpClass)


            * [`FeffAtomsTest.test_absorber_line()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_absorber_line)


            * [`FeffAtomsTest.test_absorbing_atom()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_absorbing_atom)


            * [`FeffAtomsTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_as_dict_and_from_dict)


            * [`FeffAtomsTest.test_atoms_from_file()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_atoms_from_file)


            * [`FeffAtomsTest.test_cluster_from_file()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_cluster_from_file)


            * [`FeffAtomsTest.test_distances()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_distances)


            * [`FeffAtomsTest.test_get_string()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_get_string)


            * [`FeffAtomsTest.test_single_absorbing_atom()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffAtomsTest.test_single_absorbing_atom)


        * [`FeffPotTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffPotTest)


            * [`FeffPotTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffPotTest.test_as_dict_and_from_dict)


            * [`FeffPotTest.test_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffPotTest.test_init)


            * [`FeffPotTest.test_single_absorbing_atom()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffPotTest.test_single_absorbing_atom)


        * [`FeffTagsTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffTagsTest)


            * [`FeffTagsTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffTagsTest.test_as_dict_and_from_dict)


            * [`FeffTagsTest.test_diff()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffTagsTest.test_diff)


            * [`FeffTagsTest.test_eels_tags()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffTagsTest.test_eels_tags)


            * [`FeffTagsTest.test_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.FeffTagsTest.test_init)


        * [`HeaderTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.HeaderTest)


            * [`HeaderTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.HeaderTest.test_as_dict_and_from_dict)


            * [`HeaderTest.test_from_string()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.HeaderTest.test_from_string)


            * [`HeaderTest.test_get_string()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.HeaderTest.test_get_string)


            * [`HeaderTest.test_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.HeaderTest.test_init)


        * [`PathsTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.PathsTest)


            * [`PathsTest.setUp()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.PathsTest.setUp)


            * [`PathsTest.test_paths_string()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_inputs.PathsTest.test_paths_string)


    * [pymatgen.io.feff.tests.test_outputs module](pymatgen.io.feff.tests.md#module-pymatgen.io.feff.tests.test_outputs)


        * [`FeffLdosTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest)


            * [`FeffLdosTest.filepath1`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.filepath1)


            * [`FeffLdosTest.filepath2`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.filepath2)


            * [`FeffLdosTest.ldos`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.ldos)


            * [`FeffLdosTest.reci_dos`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.reci_dos)


            * [`FeffLdosTest.reci_feffinp`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.reci_feffinp)


            * [`FeffLdosTest.reci_ldos`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.reci_ldos)


            * [`FeffLdosTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_as_dict_and_from_dict)


            * [`FeffLdosTest.test_complete_dos()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_complete_dos)


            * [`FeffLdosTest.test_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_init)


            * [`FeffLdosTest.test_reci_charge()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_reci_charge)


            * [`FeffLdosTest.test_reci_complete_dos()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_reci_complete_dos)


            * [`FeffLdosTest.test_reci_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.FeffLdosTest.test_reci_init)


        * [`XmuTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.XmuTest)


            * [`XmuTest.test_as_dict_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.XmuTest.test_as_dict_and_from_dict)


            * [`XmuTest.test_init()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_outputs.XmuTest.test_init)


    * [pymatgen.io.feff.tests.test_sets module](pymatgen.io.feff.tests.md#module-pymatgen.io.feff.tests.test_sets)


        * [`FeffInputSetTest`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest)


            * [`FeffInputSetTest.setUpClass()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.setUpClass)


            * [`FeffInputSetTest.test_charged_structure()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_charged_structure)


            * [`FeffInputSetTest.test_eels_tags_set()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_eels_tags_set)


            * [`FeffInputSetTest.test_eels_to_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_eels_to_from_dict)


            * [`FeffInputSetTest.test_get_feffPot()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_get_feffPot)


            * [`FeffInputSetTest.test_get_feff_atoms()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_get_feff_atoms)


            * [`FeffInputSetTest.test_get_header()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_get_header)


            * [`FeffInputSetTest.test_getfefftags()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_getfefftags)


            * [`FeffInputSetTest.test_large_systems()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_large_systems)


            * [`FeffInputSetTest.test_number_of_kpoints()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_number_of_kpoints)


            * [`FeffInputSetTest.test_post_distdiff()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_post_distdiff)


            * [`FeffInputSetTest.test_postfeffset()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_postfeffset)


            * [`FeffInputSetTest.test_reciprocal_tags_and_input()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_reciprocal_tags_and_input)


            * [`FeffInputSetTest.test_small_system_EXAFS()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_small_system_EXAFS)


            * [`FeffInputSetTest.test_to_and_from_dict()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_to_and_from_dict)


            * [`FeffInputSetTest.test_user_tag_settings()`](pymatgen.io.feff.tests.md#pymatgen.io.feff.tests.test_sets.FeffInputSetTest.test_user_tag_settings)



## pymatgen.io.feff.inputs module

This module defines classes for reading/manipulating/writing the main sections
of FEFF input file(feff.inp), namely HEADER, ATOMS, POTENTIAL and the program
control tags.

XANES and EXAFS input files, are available, for non-spin case at this time.


### _class_ pymatgen.io.feff.inputs.Atoms(struct, absorbing_atom, radius)
Bases: `MSONable`

Atomic cluster centered around the absorbing atom.


* **Parameters**


    * **struct** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input structure


    * **absorbing_atom** (*str/int*) – Symbol for absorbing atom or site index


    * **radius** (*float*) – radius of the atom cluster in Angstroms.



#### _static_ atoms_string_from_file(filename)
Reads atomic shells from file such as feff.inp or ATOMS file
The lines are arranged as follows:

x y z   ipot    Atom Symbol   Distance   Number

with distance being the shell radius and ipot an integer identifying
the potential used.


* **Parameters**

    **filename** – File name containing atomic coord data.



* **Returns**

    Atoms string.



#### _property_ cluster()
Returns the atomic cluster as a Molecule object.


#### _static_ cluster_from_file(filename)
Parse the feff input file and return the atomic cluster as a Molecule
object.


* **Parameters**

    **filename** (*str*) – path the feff input file



* **Returns**

    the atomic cluster as Molecule object. The absorbing atom

        is the one at the origin.




* **Return type**

    [Molecule](pymatgen.core.md#pymatgen.core.structure.Molecule)



#### get_lines()
Returns a list of string representations of the atomic configuration
information(x, y, z, ipot, atom_symbol, distance, id).


* **Returns**

    lines sorted by the distance from the absorbing atom.



* **Return type**

    list[list[str | int]]



#### write_file(filename='ATOMS')
Write Atoms list to file.


* **Parameters**

    **filename** – path for file to be written



### _exception_ pymatgen.io.feff.inputs.FeffParseError()
Bases: [`ParseError`](pymatgen.io.md#pymatgen.io.core.ParseError)

Exception class for Structure.
Raised when the structure has problems, e.g., atoms that are too close.


### _class_ pymatgen.io.feff.inputs.Header(struct: [Structure](pymatgen.core.md#pymatgen.core.structure.Structure) | [Molecule](pymatgen.core.md#pymatgen.core.structure.Molecule), source: str = '', comment: str = '', spacegroup_analyzer_settings=None)
Bases: `MSONable`

Creates Header for the FEFF input file.

Has the following format:

```default
* This feff.inp file generated by pymatgen, materialsproject.org
TITLE comment:
TITLE Source: CoO19128.cif
TITLE Structure Summary: (Co2 O2)
TITLE Reduced formula: CoO
TITLE space group: P1,   space number: 1
TITLE abc: 3.297078 3.297078 5.254213
TITLE angles: 90.0 90.0 120.0
TITLE sites: 4
* 1 Co     0.666666     0.333332     0.496324
* 2 Co     0.333333     0.666667     0.996324
* 3 O     0.666666     0.333332     0.878676
* 4 O     0.333333     0.666667     0.378675
```


* **Parameters**


    * **struct** – Structure or Molecule object. If a Structure, SpaceGroupAnalyzer is used to
    determine symmetrically-equivalent sites. If a Molecule, there is no symmetry
    checking.


    * **source** – User supplied identifier, i.e. for Materials Project this
    would be the material ID number


    * **comment** – Comment for first header line


    * **spacegroup_analyzer_settings** – keyword arguments passed to SpacegroupAnalyzer
    (only used for Structure inputs).



#### _property_ formula()
Formula of structure.


#### _static_ from_cif_file(cif_file, source='', comment='')
Static method to create Header object from cif_file.


* **Parameters**


    * **cif_file** – cif_file path and name


    * **source** – User supplied identifier, i.e. for Materials Project this
    would be the material ID number


    * **comment** – User comment that goes in header



* **Returns**

    Header Object



#### _static_ from_file(filename)
Returns Header object from file.


#### _static_ from_str(header_str)
Reads Header string and returns Header object if header was
generated by pymatgen.
Note: Checks to see if generated by pymatgen, if not it is impossible

> to generate structure object so it is not possible to generate
> header object and routine ends.


* **Parameters**

    **header_str** – pymatgen generated feff.inp header



* **Returns**

    Structure object.



#### _classmethod_ from_string(\*args, \*\*kwargs)
from_string is deprecated!
Use from_str instead


#### _static_ header_string_from_file(filename='feff.inp')
Reads Header string from either a HEADER file or feff.inp file
Will also read a header from a non-pymatgen generated feff.inp file.


* **Parameters**

    **filename** – File name containing the Header data.



* **Returns**

    Reads header string.



#### _property_ structure_symmetry()
Returns space number and space group.


* **Returns**

    Space number and space group list



#### write_file(filename='HEADER')
Writes Header into filename on disk.


* **Parameters**

    **filename** – Filename and path for file to be written to disk



### _class_ pymatgen.io.feff.inputs.Paths(atoms, paths, degeneracies=None)
Bases: `MSONable`

Set FEFF scattering paths(‘paths.dat’ file used by the ‘genfmt’ module).


* **Parameters**


    * **atoms** (*Atoms*) – Atoms object


    * **paths** (*list**(**list**)*) – list of paths. Each path is a list of atom indices in the atomic
    cluster(the molecular cluster created by Atoms class).
    e.g. [[0, 1, 2], [5, 9, 4, 1]] -> 2 paths: one with 3 legs and the other with 4 legs.


    * **degeneracies** (*list*) – list of degeneracies, one for each path. Set to 1 if not specified.



#### write_file(filename='paths.dat')
Write paths.dat.


### _class_ pymatgen.io.feff.inputs.Potential(struct, absorbing_atom)
Bases: `MSONable`

FEFF atomic potential.


* **Parameters**


    * **struct** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – Structure object.


    * **absorbing_atom** (*str/int*) – Absorbing atom symbol or site index.



#### _static_ pot_dict_from_string(pot_data)
Creates atomic symbol/potential number dictionary
forward and reverse.

Arg:

    pot_data: potential data in string format


* **Returns**

    forward and reverse atom symbol and potential number dictionaries.



#### _static_ pot_string_from_file(filename='feff.inp')
Reads Potential parameters from a feff.inp or FEFFPOT file.
The lines are arranged as follows:

> ipot   Z   element   lmax1   lmax2   stoichometry   spinph


* **Parameters**

    **filename** – file name containing potential data.



* **Returns**

    FEFFPOT string.



#### write_file(filename='POTENTIALS')
Write to file.


* **Parameters**

    **filename** – filename and path to write potential file to.



### _class_ pymatgen.io.feff.inputs.Tags(params=None)
Bases: `dict`

FEFF control parameters.


* **Parameters**

    **params** – A set of input parameters as a dictionary.



#### as_dict()
Dict representation.


* **Returns**

    Dictionary of parameters from fefftags object



#### diff(other)
Diff function. Compares two PARAMETER files and indicates which
parameters are the same and which are not. Useful for checking whether
two runs were done using the same parameters.


* **Parameters**

    **other** – The other PARAMETER dictionary to compare to.



* **Returns**

    parameters_that_are_the_same,
    “Different”: parameters_that_are_different} Note that the
    parameters are return as full dictionaries of values.



* **Return type**

    Dict of the format {“Same”



#### _static_ from_dict(d)
Creates Tags object from a dictionary.


* **Parameters**

    **d** – Dict of feff parameters and values.



* **Returns**

    Tags object



#### _static_ from_file(filename='feff.inp')
Creates a Feff_tag dictionary from a PARAMETER or feff.inp file.


* **Parameters**

    **filename** – Filename for either PARAMETER or feff.inp file



* **Returns**

    Feff_tag object



#### get_string(sort_keys=False, pretty=False)
Returns a string representation of the Tags. The reason why this
method is different from the __str__ method is to provide options
for pretty printing.


* **Parameters**


    * **sort_keys** – Set to True to sort the Feff parameters alphabetically.
    Defaults to False.


    * **pretty** – Set to True for pretty aligned output. Defaults to False.



* **Returns**

    String representation of Tags.



#### _static_ proc_val(key, val)
Static helper method to convert Feff parameters to proper types, e.g.
integers, floats, lists, etc.


* **Parameters**


    * **key** – Feff parameter key


    * **val** – Actual value of Feff parameter.



#### write_file(filename='PARAMETERS')
Write Tags to a Feff parameter tag file.


* **Parameters**

    **filename** – filename and path to write to.



### pymatgen.io.feff.inputs.get_absorbing_atom_symbol_index(absorbing_atom, structure)
Return the absorbing atom symbol and site index in the given structure.


* **Parameters**


    * **absorbing_atom** (*str/int*) – symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) –



* **Returns**

    symbol and site index



* **Return type**

    str, int



### pymatgen.io.feff.inputs.get_atom_map(structure, absorbing_atom=None)
Returns a dict that maps each atomic symbol to a unique integer starting
from 1.


* **Parameters**


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) –


    * **absorbing_atom** (*str*) – symbol



* **Returns**

    dict


## pymatgen.io.feff.outputs module

This module defines classes for parsing the FEFF output files.

Currently supports the xmu.dat, ldos.dat output files are for non-spin case.


### _class_ pymatgen.io.feff.outputs.Eels(data)
Bases: `MSONable`

Parse’eels.dat’ file.


* **Parameters**

    **(****)** (*data*) – Eels data.



#### as_dict()
Returns dict representations of Xmu object.


#### _property_ atomic_background()
atomic background.


* **Type**

    Returns



#### _property_ energies()
Returns the energies in eV.


#### _property_ fine_structure()
Fine structure of EELS.


* **Type**

    Returns



#### _static_ from_file(eels_dat_file='eels.dat')
Parse eels spectrum.


* **Parameters**

    **eels_dat_file** (*str*) – filename and path for eels.dat



* **Returns**

    Eels object



#### _property_ total_spectrum()
Returns the total eels spectrum.


### _class_ pymatgen.io.feff.outputs.LDos(complete_dos, charge_transfer)
Bases: `MSONable`

Parser for ldos files ldos01, ldos02, …..


* **Parameters**


    * **complete_dos** ([*CompleteDos*](pymatgen.electronic_structure.md#pymatgen.electronic_structure.dos.CompleteDos)) – complete dos object


    * **charge_transfer** (*dict*) – computed charge transfer between atoms
    dictionary.



#### _static_ charge_transfer_from_file(feff_inp_file, ldos_file)
Get charge transfer from file.


* **Parameters**


    * **feff_inp_file** (*str*) – name of feff.inp file for run


    * **ldos_file** (*str*) – ldos filename for run, assume consecutive order,
    i.e., ldos01.dat, ldos02.dat….



* **Returns**

    dictionary of dictionaries in order of potential sites
    ({“p”: 0.154, “s”: 0.078, “d”: 0.0, “tot”: 0.232}, …)



#### charge_transfer_to_string()
Returns charge transfer as string.


#### _static_ from_file(feff_inp_file='feff.inp', ldos_file='ldos')
Creates LDos object from raw Feff ldos files by
by assuming they are numbered consecutively, i.e. ldos01.dat
ldos02.dat…


* **Parameters**


    * **feff_inp_file** (*str*) – input file of run to obtain structure


    * **ldos_file** (*str*) – output ldos file of run to obtain dos info, etc.



### _class_ pymatgen.io.feff.outputs.Xmu(header, parameters, absorbing_atom, data)
Bases: `MSONable`

Parser for data in ‘xmu.dat’ file.
The file ‘xmu.dat’ contains XANES, EXAFS or NRIXS data depending on the
situation; \\mu, \\mu_0, and \\chi = \\chi \* \\mu_0/ \\mu_0/(edge+50eV) as
functions of absolute energy E, relative energy E - E_f and wave number k.

Default attributes:

    xmu: Photon absorption cross section of absorbing atom in material
    Energies: Energies of data point
    relative_energies: E - E_fermi
    wavenumber: k=\\sqrt(E -E_fermi)
    mu: The total absorption cross-section.
    mu0: The embedded atomic background absorption.
    chi: fine structure.
    Edge: Aborption Edge
    Absorbing atom: Species of absorbing atom
    Material: Formula of material
    Source: Source of structure
    Calculation: Type of Feff calculation performed


* **Parameters**


    * **header** – Header object


    * **parameters** – Tags object


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or index


    * **data** (*numpy.ndarray**, **Nx6*) – cross_sections.



#### as_dict()
Returns dict representations of Xmu object.


#### _property_ calc()
Returns type of Feff calculation, XANES or EXAFS.


#### _property_ chi()
Returns the normalized fine structure.


#### _property_ e_fermi()
Returns the Fermi level in eV.


#### _property_ edge()
Returns excitation edge.


#### _property_ energies()
Returns the absolute energies in eV.


#### _static_ from_file(xmu_dat_file='xmu.dat', feff_inp_file='feff.inp')
Get Xmu from file.


* **Parameters**


    * **xmu_dat_file** (*str*) – filename and path for xmu.dat


    * **feff_inp_file** (*str*) – filename and path of feff.inp input file



* **Returns**

    Xmu object



#### _property_ material_formula()
Returns chemical formula of material from feff.inp file.


#### _property_ mu()
Returns the total absorption cross-section.


#### _property_ mu0()
Returns the embedded atomic background absorption.


#### _property_ relative_energies()
Returns energy with respect to the Fermi level.
E - E_f.


#### _property_ source()
Returns source identification from Header file.


#### _property_ wavenumber()
Returns The wave number in units of \\AA^-1. k=\\sqrt(E - E_f) where E is
the energy and E_f is the Fermi level computed from electron gas theory
at the average interstitial charge density.

## pymatgen.io.feff.sets module

This module defines the FeffInputSet abstract base class and a concrete
implementation for the Materials Project. The basic concept behind an input
set is to specify a scheme to generate a consistent set of Feff inputs from a
structure without further user intervention. This ensures comparability across
runs.


### _class_ pymatgen.io.feff.sets.AbstractFeffInputSet()
Bases: `MSONable`

Abstract base class representing a set of Feff input parameters.
The idea is that using a FeffInputSet, a complete set of input files
(feffPOT, feffXANES, feffEXAFS, ATOMS, feff.inp)set_
can be generated in an automated fashion for any structure.


#### all_input()
Returns all input files as a dict of {filename: feffio object}.


#### _abstract property_ atoms()
Returns Atoms string from a structure that goes in feff.inp file.


* **Returns**

    Atoms object.



#### _abstract_ header()
Returns header to be used in feff.inp file from a pymatgen structure.


#### _abstract property_ potential()
Returns POTENTIAL section used in feff.inp from a structure.


#### _abstract property_ tags()
Returns standard calculation parameters.


#### write_input(output_dir='.', make_dir_if_not_present=True)
Writes a set of FEFF input to a directory.


* **Parameters**


    * **output_dir** – Directory to output the FEFF input files


    * **make_dir_if_not_present** – Set to True if you want the directory (
    and the whole path) to be created if it is not present.



### _class_ pymatgen.io.feff.sets.FEFFDictSet(absorbing_atom: str | int, structure: [Structure](pymatgen.core.md#pymatgen.core.structure.Structure) | [Molecule](pymatgen.core.md#pymatgen.core.structure.Molecule), radius: float, config_dict: dict, edge: str = 'K', spectrum: str = 'EXAFS', nkpts=1000, user_tag_settings: dict | None = None, spacegroup_analyzer_settings: dict | None = None)
Bases: `AbstractFeffInputSet`

Standard implementation of FeffInputSet, which can be extended by specific
implementations.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** – Structure or Molecule object. If a Structure, SpaceGroupAnalyzer is used to
    determine symmetrically-equivalent sites. If a Molecule, there is no symmetry
    checking.


    * **radius** (*float*) – cluster radius


    * **config_dict** (*dict*) – control tag settings dict


    * **edge** (*str*) – absorption edge


    * **spectrum** (*str*) – type of spectrum to calculate, available options :
    EXAFS, XANES, DANES, XMCD, ELNES, EXELFS, FPRIME, NRIXS, XES.
    The default is EXAFS.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings. To delete
    tags, set the key ‘_del’ in the user_tag_settings.
    eg: user_tag_settings={“_del”: [“COREHOLE”, “EXCHANGE”]}
    To specify a net charge on the structure, pass an “IONS” tag containing a list

    > of tuples where the first element is the unique potential value (ipot value)
    > and the second element is the charge to be applied to atoms associated
    > with that potential, e.g. {“IONS”: [(0, 0.1), (1, 0.1), (2, 0.1)]}
    > will result in.

    > ION 0 0.1
    > ION 1 0.1
    > ION 2 0.1

    > being written to the input file.



    * **spacegroup_analyzer_settings** (*dict*) – parameters passed to SpacegroupAnalyzer.
    E.g., {“symprec”: 0.01, “angle_tolerance”: 4}



#### _property_ atoms(_: Atom_ )
absorber + the rest.


* **Returns**

    Atoms



#### _static_ from_directory(input_dir)
Read in a set of FEFF input files from a directory, which is
useful when existing FEFF input needs some adjustment.


#### header(source: str = '', comment: str = '')
Creates header string from structure object.


* **Parameters**


    * **source** – Source identifier used to create structure, can be defined
    however user wants to organize structures, calculations, etc.
    example would be Materials Project material ID number.


    * **comment** – comment to include in header



* **Returns**

    Header



#### _property_ potential(_: Potentia_ )
FEFF potential.


* **Returns**

    Potential



#### _property_ tags(_: Tag_ )
FEFF job parameters.


* **Returns**

    Tags



### _class_ pymatgen.io.feff.sets.MPEELSDictSet(absorbing_atom, structure, edge, spectrum, radius, beam_energy, beam_direction, collection_angle, convergence_angle, config_dict, user_eels_settings=None, nkpts: int = 1000, user_tag_settings: dict | None = None, \*\*kwargs)
Bases: `FEFFDictSet`

FeffDictSet for ELNES spectroscopy.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input structure


    * **edge** (*str*) – absorption edge


    * **spectrum** (*str*) – ELNES or EXELFS


    * **radius** (*float*) – cluster radius in Angstroms.


    * **beam_energy** (*float*) – Incident beam energy in keV


    * **beam_direction** (*list*) – Incident beam direction. If None, the
    cross section will be averaged.


    * **collection_angle** (*float*) – Detector collection angle in mrad.


    * **convergence_angle** (*float*) – Beam convergence angle in mrad.


    * **user_eels_settings** (*dict*) – override default EELS config.
    See MPELNESSet.yaml for supported keys.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings


    * **\*\*kwargs** – Passthrough to FEFFDictSet.



### _class_ pymatgen.io.feff.sets.MPELNESSet(absorbing_atom, structure, edge: str = 'K', radius: float = 10.0, beam_energy: float = 100, beam_direction=None, collection_angle: float = 1, convergence_angle: float = 1, user_eels_settings=None, nkpts: int = 1000, user_tag_settings: dict | None = None, \*\*kwargs)
Bases: `MPEELSDictSet`

FeffDictSet for ELNES spectroscopy.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input structure


    * **edge** (*str*) – absorption edge


    * **radius** (*float*) – cluster radius in Angstroms.


    * **beam_energy** (*float*) – Incident beam energy in keV


    * **beam_direction** (*list*) – Incident beam direction. If None, the
    cross section will be averaged.


    * **collection_angle** (*float*) – Detector collection angle in mrad.


    * **convergence_angle** (*float*) – Beam convergence angle in mrad.


    * **user_eels_settings** (*dict*) – override default EELS config.
    See MPELNESSet.yaml for supported keys.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings


    * **\*\*kwargs** – Passthrough to FEFFDictSet.



#### CONFIG(_ = {'CONTROL': '1 1 1 1 1 1', 'COREHOLE': 'FSR', 'EDGE': 'K', 'ELNES': {'ANGLES': '1 1', 'BEAM_DIRECTION': '0 1 0', 'BEAM_ENERGY': '100 0 1 1', 'ENERGY': '4 0.04 0.1', 'MESH': '50 1', 'POSITION': '0.0 0.0'}, 'EXCHANGE': '0 0.0 0.0 2', 'FMS': '7.5 0', 'LDOS': '-20.0 20.0 0.1', 'PRINT': '1 0 0 0 0 0', 'S02': 0.0, 'SCF': '6.0 0 30 0.2 1'_ )

### _class_ pymatgen.io.feff.sets.MPEXAFSSet(absorbing_atom, structure, edge: str = 'K', radius: float = 10.0, nkpts: int = 1000, user_tag_settings: dict | None = None, \*\*kwargs)
Bases: `FEFFDictSet`

FeffDictSet for EXAFS spectroscopy.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input structure


    * **edge** (*str*) – absorption edge


    * **radius** (*float*) – cluster radius in Angstroms.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings


    * **\*\*kwargs** – Passthrough to FEFFDictSet.



#### CONFIG(_ = {'CONTROL': '1 1 1 1 1 1', 'COREHOLE': 'FSR', 'EDGE': 'K', 'EXAFS': 20, 'PRINT': '1 0 0 0 0 0', 'RPATH': 10, 'S02': 0.0, 'SCF': '4.5 0 30 .2 1'_ )

### _class_ pymatgen.io.feff.sets.MPEXELFSSet(absorbing_atom, structure, edge='K', radius: float = 10.0, beam_energy: float = 100, beam_direction=None, collection_angle: float = 1, convergence_angle: float = 1, user_eels_settings=None, nkpts: int = 1000, user_tag_settings: dict | None = None, \*\*kwargs)
Bases: `MPEELSDictSet`

FeffDictSet for EXELFS spectroscopy.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input structure


    * **edge** (*str*) – absorption edge


    * **radius** (*float*) – cluster radius in Angstroms.


    * **beam_energy** (*float*) – Incident beam energy in keV


    * **beam_direction** (*list*) – Incident beam direction. If None, the
    cross section will be averaged.


    * **collection_angle** (*float*) – Detector collection angle in mrad.


    * **convergence_angle** (*float*) – Beam convergence angle in mrad.


    * **user_eels_settings** (*dict*) – override default EELS config.
    See MPEXELFSSet.yaml for supported keys.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings


    * **\*\*kwargs** – Passthrough to FEFFDictSet.



#### CONFIG(_ = {'CONTROL': '1 1 1 1 1 1', 'COREHOLE': 'FSR', 'EDGE': 'K', 'EXCHANGE': '0 0.0 0.0 2', 'EXELFS': {'ANGLES': '1 1', 'BEAM_DIRECTION': '0 1 0', 'BEAM_ENERGY': '100 0 1 1', 'ENERGY': 20, 'MESH': '50 1', 'POSITION': '0.0 0.0'}, 'PRINT': '1 0 0 0 0 0', 'RPATH': 10, 'S02': 0.0, 'SCF': '5.0 0 30 0.2 1'_ )

### _class_ pymatgen.io.feff.sets.MPXANESSet(absorbing_atom, structure, edge: str = 'K', radius: float = 10.0, nkpts: int = 1000, user_tag_settings: dict | None = None, \*\*kwargs)
Bases: `FEFFDictSet`

FeffDictSet for XANES spectroscopy.


* **Parameters**


    * **absorbing_atom** (*str/int*) – absorbing atom symbol or site index


    * **structure** ([*Structure*](pymatgen.core.md#pymatgen.core.structure.Structure)) – input


    * **edge** (*str*) – absorption edge


    * **radius** (*float*) – cluster radius in Angstroms.


    * **nkpts** (*int*) – Total number of kpoints in the brillouin zone. Used
    only when feff is run in the reciprocal space mode.


    * **user_tag_settings** (*dict*) – override default tag settings


    * **\*\*kwargs** – Passthrough to FEFFDictSet.



#### CONFIG(_ = {'CONTROL': '1 1 1 1 1 1', 'COREHOLE': 'FSR', 'EDGE': 'K', 'EXCHANGE': '0 0.0 0.0 2', 'FMS': '7.5 0', 'LDOS': '-30. 15. .1', 'PRINT': '1 0 0 0 0 0', 'S02': 0.0, 'SCF': '4.5 0 30 .2 1', 'XANES': '3.7 .04 .1'_ )