#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import pytest
import os
from ase.io import read
from glob import glob
from cifcheck import utils

THIS_DIR = os.path.dirname(__file__)


@pytest.fixture(scope='module')
def get_good_paths():
    return glob(os.path.join(THIS_DIR, "correct_structures", "*.cif"))


def _paths_to_array_list(paths):
    arrays = []

    for p in paths:
        atoms = read(p, reader='pycodcif')
        arrays.append(utils._ase_to_coord_matrix(atoms))

    return arrays


@pytest.fixture(scope='module')
def get_clashing_arrays():
    _paths = ["015.cif", "017.cif", "020.cif"]

    paths = [os.path.join(THIS_DIR, "defective_structures", p) for p in _paths]

    return _paths_to_array_list(paths)


@pytest.fixture(scope='module')
def get_good_arrays():
    paths = glob(os.path.join(THIS_DIR, "correct_structures", "*.cif"))
    return _paths_to_array_list(paths)
