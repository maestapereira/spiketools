"""Position related functions."""

import numpy as np

from spiketools.utils.checks import check_array_orientation

###################################################################################################
###################################################################################################

def compute_distance(p1, p2):
    """Compute the distance between two positions.

    Parameters
    ----------
    p1, p2 : list of float
        The position values of the two positions to calculate distance between.
        Can be 1d (a single value per position) or 2d (x and y values per position).

    Returns
    -------
    float
        Distance between the two positions.

    Examples
    --------
    Compute distance between two 1d positions:

    >>> p1, p2 = [2], [5]
    >>> compute_distance(p1, p2)
    3.0

    Compute distance between the two 2d positions:

    >>> p1 = [1, 6]
    >>> p2 = [5, 9]
    >>> compute_distance(p1, p2)
    5.0
    """

    return np.linalg.norm(np.array(p1) - np.array(p2))


def compute_distances(position):
    """Compute distances across a sequence of positions.

    Parameters
    ----------
    position : 1d or 2d array
        Position values.

    Returns
    -------
    1d array
        Vector of distances between positions.

    Examples
    --------
    Compute distances across a sequence of 1d positions:

    >>> position = np.array([1., 2., 4., 5.])
    >>> compute_distances(position)
    array([1., 2., 1.])

    Compute distances across a sequence of 2d positions:

    >>> position = np.array([[1, 2, 2, 3],
    ...                      [1, 1, 2, 3]])
    >>> compute_distances(position)
    array([1.        , 1.        , 1.41421356])
    """

    position = position.T if check_array_orientation(position) == 'row' else position

    dists = np.zeros(len(position) - 1)
    for ix, (p1, p2) in enumerate(zip(position, position[1:])):
        dists[ix] = compute_distance(p1, p2)

    return dists


def compute_cumulative_distances(position):
    """Compute cumulative distance across a sequence of positions.

    Parameters
    ----------
    position : 1d or 2d array
        Position values.

    Returns
    -------
    1d array
        Cumulative distances.

    Examples
    --------
    Compute cumulative distances across a sequence of 1d positions:

    >>> position = np.array([1., 2., 4., 5.])
    >>> compute_cumulative_distances(position)
    array([1., 3., 4.])

    Compute cumulative distances across a sequence of 2d positions:

    >>> position = np.array([[1, 2, 2, 3],
    ...                      [1, 1, 2, 3]])
    >>> compute_cumulative_distances(position)
    array([1.        , 2.        , 3.41421356])
    """

    return np.cumsum(compute_distances(position))


def compute_distances_to_location(position, location):
    """Compute distances between a sequence of positions and a specified location.

    Parameters
    ----------
    position : 1d or 2d array
        Position values.
    location : list of float
        The position values of the two positions to calculate distance between.
        Can be 1d (a single value per position) or 2d (x and y values per position).

    Returns
    -------
    dists : 1d array
        Computed distances between each position in the sequence, and the specified location.
    """

    position = position.T if check_array_orientation(position) == 'row' else position

    dists = np.zeros(len(position))
    for ix, pos in enumerate(position):
        dists[ix] = compute_distance(pos, location)

    return dists


def compute_speed(position, bin_times):
    """Compute speeds across a sequence of positions.

    Parameters
    ----------
    position : 1d or 2d array
        Position values.
    bin_times : 1d array
        Times spent traversing each position bin.

    Returns
    -------
    speed : 1d array
        Vector of speeds across each position step.

    Examples
    --------
    Compute speed across a sequence of 1d positions:

    >>> position = np.array([1., 2., 4., 5.])
    >>> bin_times = np.array([1, 1, 0.5])
    >>> compute_speed(position, bin_times)
    array([1., 2., 2.])

    Compute speed across a sequence of 2d positions:

    >>> position = np.array([[1, 2, 2, 3],
    ...                      [1, 1, 2, 3]])
    >>> bin_times = np.array([1, 0.5, 1])
    >>> compute_speed(position, bin_times)
    array([1.        , 2.        , 1.41421356])
    """

    distances = compute_distances(position)
    speed = distances / bin_times

    return speed
