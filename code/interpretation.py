"""Interpret the clusterized data."""

import os

import control
import matplotlib.pyplot as plt
import seaborn as sns


def print_feature(feature):
    """Prints a feature in a nice way (aesthetics)."""
    feature = feature + '   '
    print('\n{0:-<70s}\n'.format(feature), 70*'-', sep='')
    return None


def describe_clusters(dataframe):
    """Describe clusters and give them interpretability."""
    gb = dataframe.groupby('cluster')

    print_feature('N per cluster')
    print(gb.count()['id'])

    print_feature('Cluster standard deviation of variables')
    cluster_std = gb.std()
    all_std = dataframe.std()
    all_std.loc['cluster'] = 'all'
    all_std.name = 'all'
    cluster_std = cluster_std.append(all_std.T).drop('cluster', axis=1)
    print(cluster_std)

    title = 'Cluster mean of variables'
    cluster_mean = gb.mean()
    all_mean = dataframe.mean()
    all_mean.loc['cluster'] = 'all'
    all_mean.name = 'all'
    cluster_mean = cluster_mean.append(all_mean.T).drop('cluster', axis=1)
    plot_cluster_analysis(cluster_mean, cluster_std, title)
    print_feature(title)
    print(cluster_mean)

    print_feature('Normalized cluster standard deviation of variables')
    print(cluster_std/cluster_std.max())

    print_feature('Normalized cluster mean')
    print(gb.mean()/gb.mean().max())


def plot_cluster_analysis(dataframe, error, title):
    """Plot cluster analysis on the same figure."""
    for column in dataframe:
        fig, ax = plt.subplots()
        ax = sns.barplot(x=dataframe.index,
                         y=dataframe[column],
                         # estimator=mean x: x,
                         yerr=error[column],
                         )
        filename = (
            'cluster_analysis' + '_'
            + title.lower().replace(' ', '_') + '_'
            + column.lower().replace(' ', '_') + '.png')
        fig.savefig(
            os.path.join(control.CLUSTERING_PATH, filename),
            dpi=300)



if __name__ == '__main__':
    print_feature('abba')
    print_feature('cab cab')
