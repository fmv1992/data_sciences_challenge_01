# Code challenge easynvest

# Description

This is the complete document of the challenge proposed by Easynvest.
Disclosure of company name and publishing of the results were explicitly
authorized by their recruiting team.

Easynvest is a fintech company, more specifically a digital broker-dealer which
helps thousands of clients to invest their money easily and quickly. They are
known for their online platform and strong digital presence.

The complete description of the challenge may be found in the file
`challenge_description/challenge_description.pdf` (in Portuguese).

# Introduction

## The data set

The data set received was in the form of an Excel spreadsheet with two tabs.
The first tab contained 4973 entries (N=4973), one unique ID and 10
characteristics.  
The second tab has entries which are not described elsewhere. The lack of a
formal description casts unecessary uncertainty into the data at hand.  Lack of
proper definition is a discouraged practice in data creation (e.g.: research
method) and methodology must not be open for interpretation.

A remarkable fact of this data set is that it does not contain any null values.
Such high quality data sets are rare to find and may indicate that its source
is very thoughtful of its data management.

A final remark is that the characteristics' names should not be considered self
explanatory. A codebook is often use to describe published data.  
To illustrate the critique above consider the variable 'VALOR_01' (value_01).
To what value does it refer to? Is it the amount already invested in the
investment platform? Is it the income enumerated by different sources of
income? Is it profit? If it is income, is it yearly or monthly?  
Another illustration is the 'GEO_REFERENCIA' (georeference) variable. It has
values ranging from 10 to 999 but it is not explained elsewhere. Usual
geolocation information are comprised of x and y coordinates or other better
known formats. Consequently this variable has been neglected in the present
analysis.

As one can see, this seemingly unimportant differences may yield different
interpretations later on the data analysis and render some conclusions useless.


* TODO: include total income/total value in dicusssion. XXX
* TODO: comment on data set: non nulls
* TODO: comment on geo_referencia

# Approach

As stated in the challenge description my work should:

1. Group users, finding well defined groups with common characteristics.
    * In order to do that I have clustered the data set using the K-Means
      clustering algorithm.

1. Justify the chosen clustering algorithm.
    * This algorithm is one of the most commonly used algorithm in Data
      Sciences. As such one can easily find support, implementations,
      discussions and suggestions on various references. Such vast amount of
      information is not something to be neglected.  
      It also allows the specification of the number of clusters to be found.
      This is seen as drawback sometimes. Yet I think that it can be overcome
      with successively running the algorithm with a different cluster number.  
      Also it tends to yield clusters with similar size. This is may be a
      desired characteristic in a business setting for example, where
      investment of resources (time and capital) may be applied to each cluster
      of clients. In such cases one does not want to invest those in a cluster
      just to find out that it aggregates to just 1% of their clientele.

1. Present metrics of perfomance for the chosen algorithm
    * In this case the silhouette analysis was performed to assess the
      effectivenss of the clustering algorithm. Also the intra-group and
      inter-group standard deviation and means were taken in consideration to
      interpret the results of this clustering algorithm.

1. Discuss the metrics of performance to assess the clusters.
    * See [discussion of the clustering](#clustering) for a complete assessment
      of the clustering algorithm.

1. Explain the results.
    * See the [results](#results) and [summary](#summary) sections for a
      precise answer to this question.

# Results {#results}

## Preprocessing
* categorical to binary
* scaling

## Clustering {#clustering}

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


# Summary {#summary}

# Additional information & Reproducibility

## Tools
* Vim
* python
```
python3 --version
Python 3.6.1
```
* python modules:
    * mod1
    * mod1
    * mod1
* pandoc
TODO

# Other remarks

* Comment on the data set ; suggest improvements.

# Next steps

* The 
