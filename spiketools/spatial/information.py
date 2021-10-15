"""Measures of spatial information."""

import warnings

import numpy as np

###################################################################################################
###################################################################################################

def compute_spatial_information_2d(spike_x, spike_y, bins, occupancy):
    """Compute spatial information across a 2d space.

    Parameters
    ----------
    spike_x, spike_y : 1d array
        Spike positions.
    bins : list of int
        Binning to use.
    occupancy : 2d array
        Occupancy of the space.

    Returns
    -------
    info : float
        Spike information rate for spatial information (bits/spike).
    """

    spike_map = np.histogram2d(spike_x, spike_y, bins=bins)[0]
    info = _compute_spatial_information(spike_map, occupancy)

    return info


def compute_spatial_information_1d(data, occupancy, bins):
    """Compute spatial information across a 1d space using Skaggs information.

    Parameters
    ----------
    data : 1d array
        Spike positions.
    occupancy : 1d array
        Occupancy data.
    bins : int
        Number of bins to use.

    Returns
    -------
    info : float
        Spike information rate for spatial information (bits/spike).
    """

    spike_map = np.histogram(data, bins=bins)[0]
    info = _compute_spatial_information(spike_map, occupancy)

    return info


def _compute_spatial_information(spike_map, occupancy):
    """Compute spatial information.

    Parameters
    ----------
    spike_map : ndarray
        Spike positions.
    occupancy : ndarray
        Occupancy.

    Returns
    -------
    info : float
        Spike information rate for spatial information (bits/spike).
    """

    # Calculate average firing rate
    rate = np.nansum(spike_map) / np.nansum(occupancy)
    if rate == 0.0:
        return 0.0

    # Compute the occupancy probability (per bin)
    occ_prob = occupancy / np.nansum(occupancy)
    
    # Supress RunTime warnings for invalid values that might occur in the arrays during calculations
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=RuntimeWarning)

        # Calculate the normalized spiking (by occupancy)
        spike_map_norm = spike_map / occupancy

        # Calculate the spatial information, using a mask for nonzero values
        nz = np.nonzero(spike_map_norm)
        info = np.nansum(occ_prob[nz] * spike_map_norm[nz] * np.log2(spike_map_norm[nz] / rate)) / rate

    return info
