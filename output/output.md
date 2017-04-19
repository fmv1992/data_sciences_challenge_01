# Code challenge easynvest

# Description

This is the complete document of the challenge.

# Introduction

# The data set

* TODO: include total income/total value in dicusssion. XXX
* TODO: comment on data set: non nulls
* TODO: comment on geo_referencia

# Approach

# Results

## Preprocessing
* categorical to binary
* scaling

## Clustering

### Choice of the number of clusters

I have chosen the numbers of clusters to be six. See the discussion below for
details.

Before diving in the details of my choice, one cannot overstress the importance
of the choice of the number of clusters. This is arguably the most tricky
decision in this challenge as it deals with a great mix of technical as well as
non-technical details.

* overstress importance

I have chosen the number of cluster to be 6 for a couple of different reasons.
First of all, analyzing the average value for silhouette we can see that the
average value for silhouette reaches a maximum at around 18 clusters.

From a pure technical standpoint choosing n_clusters such that the average
value for silhouette is maximum is the best option. On the other hand, working
with such a large number of clusters may hinder the interpretability of the
results as clusters probably would not have a sharp distinction between them
(consider that our data set has 10 dimensions originally).  
Probably the communication of such results for a multidiscipliniary team of
mixed background would be noisy as well.

In the light of such considerations one would preferably limit the number of
clusters to a maximum of ~10.

Back to the average silhouettes, we can see that it is an increasing function
between 2 and 6 clusters, almost doubling its value in this interval. This
means that the samples are on average better defined in the own cluster, and
far away from other clusters. Another fact that indicates that 6 is a good
number for clusters is that in this case just a few data points show a
silhouette smaller than zero. In other words, just a few data points are
incorrectly labeled in their cluster (those data points are unfrequent and are
concentrated on cluster 2). Using the same argumentation the cluster that is
best defined is cluster 1 because of the high incidence of data points at near
.75 silhouette value.

## Cluster interpretation

For cluster interpretation two resources are available:

1. Tables output to stdout during program execution.
1. Plots.

From a general standpoint clusters should have low intra-cluster variance and
high inter-cluster variance for each variable.

### Cluster 0

*Distinctive features:*

1. Has the most concentration of other marital status (that is, it is neither
   married nor single).
1. Has the highest age mean of all groups even though there is a high
   dispersion both intra and inter cluster for this variable.

### Cluster 1

*Distinctive features:*

1. Has the most concentration of single persons ('solteiro').
1. It is solely composed of male individuals (absence of 'genenro_f'). This
   also happens to cluster 2 and cluster 3.
1. Has the most concentration of profile D ('perfil_d'). Also contains a lot of
   profile A individuals.
1. Has the most concentration young people.

### Cluster 2

*Distinctive features:*

1. Has the highest averages for 'valor_02', 'valor_03' and 'valor_04'.
   In respect to these 3 variables all the other groups have much lower
   averages.
1. Includes almost solely profile B people.
1. Contains almost solely males.

### Cluster 3

*Distinctive features:*

1. It is the group with the highest proportion of married individuals
   ('estado_civil_casado').
1. The cluster is entirely comprised of male individuals.
1. The cluster contains only individuals from profile A and profile D.

### Cluster 4

*Distinctive features:*

1. a
1. b
1. c

### Cluster 5

*Distinctive features:*

1. a
1. b
1. c


# Summary

# Additional information & Reproducibility

## Tools
* Vim
* python
```
python3 --version
Python 3.6.1
```
* pthon modules:
TODO

## Software version

TODO

# Other remarks

* Comment on the data set 

# Next steps

* The 
