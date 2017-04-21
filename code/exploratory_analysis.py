"""Conduct exploratory analysis to better understand our data set.

Generate quick and easy visualization which may help us understand the data set
at hand.

"""
import itertools
import os

from data_utilities import matplotlib_utilities as mu

import control


def main(*args):
    """Conduct exploratory analysis to better understand our data set.

    Return None

    """
    # Create a list of figures with exploratory data.
    figures = []
    for dataframe in args:
        fig = mu.histogram_of_dataframe(
            dataframe,
            output_path=None,  # Manually save figures.
            kde=False)
        figures.append(fig)

    # Manually save figures in order to be able to rotate axes.
    figures = itertools.chain.from_iterable(figures)
    for i, fig in enumerate(figures):
        # Set names for figures.
        for ax in fig.get_axes():
            xlabel = ax.get_xlabel()
            if not xlabel:  # relabel in case of empty string
                # Use if more than one data set is passed to args.
                if len(args) > 1:
                    xlabel = i
                else:
                    xlabel = dataframe.columns[i]
            # Rotate axes.
            ax.set_xticklabels(
                ax.get_xticklabels(),
                rotation=-90)

        # Save figure.
        fig.tight_layout()
        fig.savefig(
            os.path.join(
                control.EXPL_ANALYSIS_PATH,
                '{0}.png'.format(xlabel)),
            dpi=300)

    return None
