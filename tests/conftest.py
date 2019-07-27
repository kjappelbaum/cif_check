#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import pytest
import os
from glob import glob

THIS_DIR = os.path.dirname(__file__)

@pytest.fixture(scope='module')
def get_good_paths():
    return glob(os.path.join(THIS_DIR, "correct_structures", "*.cif"))

@pytest.fixture(scope='module')
def get_clashing_arrays():
    paths = [
        "015.cif"
        "017.cif",
        "020.cif"
    ]
    return paths