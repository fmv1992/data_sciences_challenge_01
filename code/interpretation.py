"""Interpret the clusterized data.

Generate prints of various cluster information to be used in the discussion and
assessment of the clusterization.

"""

import os

import control
import matplotlib.pyplot as plt
import seaborn as sns


def print_feature(feature):
    """Print a feature in a nice and consistent way (aesthetics).

    Return None.

    """
    feature = feature + '   '
    print('\n', 70*'-', '\n{0:-<70s}\n'.format(feature), 70*'-', sep='')
    return None


def describe_clusters(dataframe):
    """Describe clusters and give them interpretability.

    Print a set of important data to stdout to enable cluster interpretation.

    Also saves plot for each cluster.

    Return None.

    """
    # Group clusters.
    gb = dataframe.groupby('cluster')

    # Show standard deviation of variables.
    print_feature('Cluster standard deviation of variables')
    cluster_std = gb.std()
    all_std = dataframe.std()
    all_std.loc['cluster'] = 'all'
    all_std.name = 'all'
    cluster_std = cluster_std.append(all_std.T).drop('cluster', axis=1)
    print(cluster_std)

    # Show mean of variables.
    title = 'Cluster mean of variables'
    cluster_mean = gb.mean()
    all_mean = dataframe.mean()
    all_mean.loc['cluster'] = 'all'
    all_mean.name = 'all'
    cluster_mean = cluster_mean.append(all_mean.T).drop('cluster', axis=1)
    print_feature(title)
    print(cluster_mean)
    # Plot the mean of variables with standard deviations/errors.
    plot_cluster_analysis(cluster_mean, cluster_std, title)

    # Show normalized standard deviation of variables.
    print_feature('Normalized cluster standard deviation of variables')
    print(cluster_std/cluster_std.max())

    # Show normalized mean of variables.
    print_feature('Normalized cluster mean')
    print(gb.mean()/gb.mean().max())

    # Show normalized sum of variables.
    print_feature('Cluster sum of variables')
    cluster_sum = gb.sum()
    print(cluster_sum)

    return None


def plot_cluster_analysis(dataframe, error, title):
    """Plot cluster analysis.

    For each available column produce a corrisponding image to enhance
    interpretability of the results.

    Return None.

    """
    for column in dataframe:
        fig, ax = plt.subplots()
        ax = sns.barplot(x=dataframe.index,  # noqa
                         y=dataframe[column],
                         yerr=error[column],
                         )
        filename = (
            'cluster_analysis' + '_'
            + title.lower().replace(' ', '_') + '_'
            + column.lower().replace(' ', '_') + '.png')
        fig.savefig(
            os.path.join(control.CLUSTERING_PATH, filename),
            dpi=300)

    return None
