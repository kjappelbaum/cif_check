#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

from cifcheck.checks import check_clashing

def test_check_clashing(get_clashing_arrays, get_good_arrays):
    for a in get_clashing_arrays:
        assert check_clashing(a, method="pdist")

    for a in get_good_arrays:
        assert not check_clashing(a, method="pdist")

    for a in get_clashing_arrays:
        assert check_clashing(a, method="kdtree")

    for a in get_good_arrays:
        assert not check_clashing(a, method="kdtree")