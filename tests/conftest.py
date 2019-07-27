#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import pytest
import os
from pymatgen import Structure
from glob import glob
from cifcheck import utils

THIS_DIR = os.path.dirname(__file__)

@pytest.fixture(scope='module')
def get_good_paths():
    return glob(os.path.join(THIS_DIR, "correct_structures", "*.cif"))

@pytest.fixture(scope='module')
def get_clashing_arrays():
    _paths = [
        "015.cif"
        "017.cif",
        "020.cif"
    ]

    paths = [os.path.join(THIS_DIR, "defective_structures", p) for p in _paths]

    arrays = []

    for p in paths:
        s = Structure.from_file(p)
        arrays.append(utils._pymatgen_to_coord_matrix(s))

    return arrays

@pytest.fixture(scope='module')
def get_good_arrays(get_good_paths):
    arrays = []

    for p in get_good_paths:
        s = Structure.from_file(p)
        arrays.append(utils._pymatgen_to_coord_matrix(s))

    return arrays




