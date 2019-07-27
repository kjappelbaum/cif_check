#!/usr/bin/python
# -*- coding: utf-8 -*-
__copyright__ = 'MIT License'
__status__ = 'First Draft, Testing'

import jax.numpy as np
from jax import grad, jit, vmap
from scipy.spatial import cKDTree
from pymatgen import Structure

from scipy.spatial.distance import pdist

def _ase_to_coord_matrix(atoms):
    return atoms.get_positions()

def _pymatgen_to_coord_matrix(structure: Structure):
    return structure.cart_coords


@jit
def _get_duplicates_list(groups):
    """
    Args:
        coord_matrix (np.array): 3 * N array of position of atoms

    Returns:
        list of duplicates
    """
    groups = [g for g in groups if len(g) >= 2]
    duplicates = []
    for g in groups:
        if len(g) > 2:
            for _, index in enumerate(g[1:]):
                duplicates.append(tuple((g[0], index)))
        else:
            duplicates.append(tuple(g))

    del groups

    duplicates = list(set(map(tuple, map(sorted, duplicates))))

    duplicates = [d for d in duplicates if d[0] != d[1]]

    return duplicates

def _get_duplicates_ktree(coord_matrix: np.array, threshold: float = 0.2) -> list:
    """

    Args:
        coord_matrix (np.array): 3 * N array of position of atoms

    Returns:
        list of duplicates
    """

    tree = cKDTree(coord_matrix)
    groups = tree.query_ball_point(coord_matrix, threshold)

    duplicates = _get_duplicates_list(groups)

    return duplicates

def _get_duplicates_pdist(coord_matrix: np.array, threshold: float = 0.2) -> list:
    """

    Args:
        coord_matrix (np.array): 3 * N array of position of atoms

    Returns:
        list of duplicates
    """
    dists = pdist(coord_matrix, 'sqeuclidean')
    dup = np.nonzero(dists < threshold ** 2)

    return list(dup)

