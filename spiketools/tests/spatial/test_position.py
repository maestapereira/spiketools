"""Tests for spiketools.spatial.position"""

import numpy as np

from spiketools.spatial.position import *

###################################################################################################
###################################################################################################

def test_compute_distance():

    out0 = compute_distance(1, 1, 1, 1)
    assert isinstance(out0, float)
    assert np.isclose(out0, 0.0)

    out1 = compute_distance(1, 1, 2, 1)
    assert isinstance(out1, float)
    assert np.isclose(out1, 1.0)

    out2 = compute_distance(1, 1, 2, 2)
    assert np.isclose(out2, np.sqrt(2))

    out3 = compute_distance(1, 1, -1, 1)
    assert np.isclose(out3, 2)

def test_compute_distances():

    xs = np.array([0, 0, 1, 1, 2])
    ys = np.array([0, 0, 0, 1, 2])

    out = compute_distances(xs, ys)
    assert isinstance(out, np.ndarray)
    assert len(out) == len(xs) -1
    assert np.allclose(out, np.array([0, 1, 1, np.sqrt(2)]))

def test_compute_cumulative_distances():

    xs = np.array([0, 1, 1, 2])
    ys = np.array([0, 0, 1, 2])

    out = compute_cumulative_distances(xs, ys)
    assert isinstance(out, np.ndarray)
    assert len(out) == len(xs)
    assert np.allclose(out, np.array([0, 1, 1 + 1, 1 + 1 + np.sqrt(2)]))

def test_compute_speed():

    xs = np.array([0, 1, 1, 2])
    ys = np.array([0, 0, 1, 2])

    timestamps1 = np.array([0, 1, 2, 3])
    out1 = compute_speed(xs, ys, timestamps1)
    assert isinstance(out1, np.ndarray)
    assert len(out1) == len(xs)
    assert np.allclose(out1, np.array([0, 1, 1, np.sqrt(2)]))

    timestamps2 = np.array([0, 1, 1.5, 2.0])
    out2 = compute_speed(xs, ys, timestamps2)
    assert isinstance(out2, np.ndarray)
    assert len(out2) == len(xs)
    assert np.allclose(out2, np.array([0, 1, 1 / 0.5, np.sqrt(2) / 0.5]))
