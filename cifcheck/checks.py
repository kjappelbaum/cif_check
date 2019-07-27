#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import jax.numpy as np
from cifcheck import utils

def check_clashing(coord_matrix: np.array, threshold: float = 0.3, method="pdist") -> bool:
    """
    Takes positions of atoms checks if there are atoms that are too close (i.e. their distance
    is smaller than the threshold).

    Args:
        coord_matrix (np.array): 3 * N array of position of atoms
        threshold (float): used as a check for clashing atoms
        method (sting): kdtree or pdist (pdist is default). Using either a more efficient cKDTree datastructure
            for querying duplicates or the pdist distance matrix implementation

    Returns:
        bool
    """

    duplicates = utils._get_duplicates_ktree(coord_matrix, threshold)

    if len(duplicates) > 1:
        return True
    else:
        return False