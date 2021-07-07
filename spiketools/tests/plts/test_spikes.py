"""Tests for spiketools.plts.spikes"""

import numpy as np

from spiketools.tests.tutils import plot_test
from spiketools.tests.tsettings import TEST_PLOTS_PATH

from spiketools.plts.spikes import *

###################################################################################################
###################################################################################################

@plot_test
def test_plot_waveform():

    data = np.array([0, 0, 0, 1, 2, 3, 4, 5, 3, 1, 0, 0])
    plot_waveform(data,
                  file_path=TEST_PLOTS_PATH, file_name='test_plot_waveform.png')

@plot_test
def test_plot_isis():

    data = np.array([0.1, 0.25, 0.4, 0.1, 0.05, 0.2, 0.125])

    plot_isis(data,
        file_path=TEST_PLOTS_PATH, file_name='test_plot_waveform.png')

@plot_test
def test_plot_firing_rates():

    data = np.array([2.5, 0.5, 1.2, 3.4])

    plot_firing_rates(data,
                      file_path=TEST_PLOTS_PATH, file_name='test_plot_firing_rates.png')