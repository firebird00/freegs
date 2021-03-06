FreeGS: Free boundary Grad-Shafranov solver
===========================================

[![License](https://img.shields.io/badge/license-GPL-blue.svg)](https://img.shields.io/badge/license-GPL-blue.svg)
[![py3comp](https://img.shields.io/badge/py3-compatible-brightgreen.svg)](https://img.shields.io/badge/py3-compatible-brightgreen.svg)

This Python module solves the Grad-Shafranov equation for axisymmetric
plasma equilibria, mainly for free boundary calculations.

Installing
----------

FreeGS is available on PyPI 

    $ pip install --user freegs

or clone/download this repository and run setup:

    $ git clone https://github.com/bendudson/freegs.git
    $ cd freegs
    $ python setup.py install --user

Documentation
-------------

The manual is in the `docs` subdirectory, and [hosted here on readthedocs](http://freegs.readthedocs.io/en/latest/).

Examples
--------

The Jupyter notebooks contain examples wuth additional notes

* MAST-example.ipynb 

There are also some Python scripts to run short tests
and examples

    $ python 01-freeboundary.py

This solves a free boundary problem, specifying the desired location of two X-points.
Writes the equilibrium to a G-EQDSK file "lsn.geqdsk"

    $ python 02-read-geqdsk.py

Reads in the file "lsn.geqdsk", inferring the coil currents from the plasma boundary
and profiles in the G-EQDSK file.

    $ python 03-mast.py

Calculates a double-null (CDND) equilibrium for MAST from scratch. Writes solution to
G-EQDSK file "mast.geqdsk"

    $ python 04-read-mast-geqdsk.py

Reads the file "mast.geqdsk", inferring the coil currents.

    $ python 05-fixed-boundary.py 

This example solves a fixed boundary problem, in which the square edges of the domain
are fixed. The plasma pressure on axis and plasma current are fixed.

    $ python 06-xpoints.py

This demonstrates the coil current control code, finding X-points, and marking core region
These routines are used inside the free boundary solver

Files
-----

The "freegs" module consists of the following files:

* **boundary.py**        - Operators for applying boundary conditions to plasma psi
* **control.py**         - Routines for controlling coil currents based on constraints
* **critical.py**        - Finds critical points (O- and X-points)
* **equilibrium.py**     - Represents the plasma equilibrium state
* **gradshafranov.py**   - Greens functions and operators for the Grad-Shafranov equation
* **jtor.py**            - Routines for calculating toroidal current density (profiles)
* **machine.py**         - Represents the coils and power supply circuits
* **multigrid.py**       - The multigrid solver for the linear elliptic operator
* **picard.py**          - Nonlinear solver, iterating the profiles and constraints
* **plotting.py**        - Plotting routines using matplotlib

License
-------

    Copyright 2016-2018 Ben Dudson, University of York. Email: benjamin.dudson@york.ac.uk

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

References
----------

* YoungMu Jeon, [Development of a free boundary Tokamak Equlibrium Solver](http://link.springer.com/article/10.3938/jkps.67.843)  [arXiv:1503.03135](https://arxiv.org/abs/1503.03135)
* S.Jardin "Computational Methods in Plasma Physics" CRC Press

