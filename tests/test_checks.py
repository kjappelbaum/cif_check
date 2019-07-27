#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

from cifcheck.checks import check_clashing

def test_check_clashing(get_clashing_arrays, get_good_arrays):
    bad = get_clashing_arrays
    good = get_good_arrays

    for a in bad:
        assert check_clashing(a, method="pdist")

    for a in good:
        assert not check_clashing(a, method="pdist")

    for a in bad:
        assert check_clashing(a, method="kdtree")

    for a in good:
        assert not check_clashing(a, method="kdtree")


