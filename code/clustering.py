"""Cluster the data."""

import os

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.preprocessing import scale
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples

import control
from interpretation import print_feature


def preprocess_data(dataframe):
    """Preprocess the data.

    Preprocess the data because K-means clustering is sensitive to
    scaling.

    Return the preprocessed dataframe.

    """
    processed_dataframe = dataframe.copy(True).apply(scale)
    print_feature('The effect of preprocessing on standard deviation')
    print('\tbefore:\n', dataframe.std(), sep='')
    print('\tafter:\n', processed_dataframe.std(), sep='')

    return processed_dataframe


def get_n_clusters(dataframe, max_clusters=10):
    """Help find the adequate number of clusters for the dataset.

    Help find the adequate number of clusters for the dataset using the
    'silhouette method'.

    Return None.

    """
    cluster_list = tuple(range(2, max_clusters))
    sil_avg_list = []
    sil_std_list = []
    cluster_labels_dict = dict()

    print_feature('Features for different number of clusters')

    for n in cluster_list:
        # Create the cluster.
        cluster = KMeans(n_clusters=n, random_state=control.RANDOM_SEED)
        cluster_labels = cluster.fit_predict(dataframe)
        cluster_labels_dict[n] = cluster_labels

        # Store average silhouette score.
        sil_avg = silhouette_score(dataframe, cluster_labels,
                                   random_state=control.RANDOM_SEED)
        sil_avg_list.append(sil_avg)

        sil_ind = silhouette_samples(dataframe, cluster_labels)

        # Store standard deviation of silhouettes score.
        sil_std = np.std(sil_ind)
        sil_std_list.append(sil_std)

        # Print results.
        print('Silhouette average for', n, 'clusters',
              '{0:1.3f}'.format(sil_avg))

        # Plot silhouettes on the same histogram for low values of cluster.
        if n <= 7:
            fig, axes = plt.subplots(n, 1, sharex=True, sharey=True,
                                     figsize=(8, 2*n))
            # Create a dataframe to groupby.
            dataframe_of_sil = pd.DataFrame(
                data={'cluster': cluster_labels,
                      'sil': sil_ind})
            # Iterate over cluster and axes
            print('Number of individuals per cluster for', n, 'clusters',
                  21*'-')
            for i in range(n):
                l = dataframe_of_sil.ix[dataframe_of_sil.cluster == i, 'sil']
                print(l.shape)
                ax = sns.distplot(
                    dataframe_of_sil.ix[dataframe_of_sil.cluster == i, 'sil'],
                    kde=False,
                    ax=axes[i],
                    norm_hist=True)
                ax.set_title('cluster {0:d}'.format(i), loc='left')
            # Set plotting preferences.
            axes[0].set_xticks([-1, -.5, 0, .5, 1])
            axes[0].set_xlim(-1, 1)
            axes[-1].set_xlabel('Silhouette distribution for clusters')
            # Save figure.
            fig.tight_layout()
            fig.savefig(
                os.path.join(
                    control.CLUSTERING_PATH,
                    'silhouette_distribution_for_n={0:d}_clusters.png'.format(
                        n)),
                dpi=300)

    # Plot the silhouette.
    fig, ax = plt.subplots()
    plt.errorbar(cluster_list, sil_avg_list, sil_std_list)
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('Average value for silhouette')
    ax.set_xticks(cluster_list[:])
    ax.set_ylim(-1, 1)
    fig.savefig(
        os.path.join(
            control.CLUSTERING_PATH,
            'silhouette.png'),
        dpi=300)

    return cluster_labels_dict


def create_120_silh_plot(dataframe):
    """Create a silhouette plot for K-Means cluster from 2 clusters to 120.

    WARNING: the running time for this function is very long (~ 7min).
    Using the keyword argument 'j_jobs' breaks in cygwin.

    Return None

    """
    cluster_list = tuple(range(2, 120))
    sil_avg_list = []
    sil_std_list = []
    cluster_labels_dict = dict()

    for n in cluster_list:
        # Create the cluster.
        cluster = KMeans(n_clusters=n,
                         random_state=control.RANDOM_SEED,
                         n_jobs=1)
        cluster_labels = cluster.fit_predict(dataframe)
        cluster_labels_dict[n] = cluster_labels

        # Store average silhouette score.
        sil_avg = silhouette_score(dataframe, cluster_labels,
                                   random_state=control.RANDOM_SEED)
        sil_avg_list.append(sil_avg)

        sil_ind = silhouette_samples(dataframe, cluster_labels)

        # Store standard deviation of silhouettes score.
        sil_std = np.std(sil_ind)
        sil_std_list.append(sil_std)

    # Plot the silhouette.
    fig, ax = plt.subplots()
    plt.errorbar(cluster_list, sil_avg_list, yerr=sil_std_list)
    ax = fig.get_axes()[0]
    ax.set_xlabel('Number of clusters')
    ax.set_ylabel('Average value for silhouette')
    ax.set_xticks(cluster_list[::10])
    ax.set_ylim(-1, 1)
    fig.savefig(
        os.path.join(
            control.CLUSTERING_PATH,
            'silhouette_120.png'),
        dpi=300)

    return cluster_labels_dict
