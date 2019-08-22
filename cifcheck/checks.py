#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import numpy as np
from cifcheck import utils
import warnings
warnings.filterwarnings('ignore', message='scaled_positions')


def check_clashing(coord_matrix: np.array,
                   threshold: float = 0.6,
                   method='pdist') -> bool:
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

    if method == 'kdtree':
        duplicates = utils._get_duplicates_ktree(coord_matrix, threshold)  # pylint:disable=protected-access
    else:
        duplicates = utils._get_duplicates_pdist(coord_matrix, threshold)  # pylint:disable=protected-access

    return bool(len(duplicates) > 1)


def check_any_hydrogen():
    raise NotImplementedError


def check_undercoordinated():
    raise NotImplementedError


def check_solvent():
    raise NotImplementedError
