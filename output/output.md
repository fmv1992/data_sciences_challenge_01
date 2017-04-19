# Code challenge easynvest

# Description

This is the complete document of the challenge.

# Introduction

# The data set

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

## Clustering

# Summary

# Additional information

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
