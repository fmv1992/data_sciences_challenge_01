"""Set variables for code challenge by Easynvest."""
import os
import numpy as np
import pandas as pd

pd.options.display.max_columns = 100
np.set_printoptions(edgeitems=7)

RANDOM_SEED = 1

DATA_PATH = '../data'
DADOS_PATH = os.path.join(
    DATA_PATH,
    'dataset_code_challenge_data_scientist_dados.csv')
DEPARA_PATH = os.path.join(
    DATA_PATH,
    'dataset_code_challenge_data_scientist_depara.csv')

OUTPUT_PATH = '../output/'
EXPL_ANALYSIS_PATH = os.path.join(
    OUTPUT_PATH,
    'exploratory_analyses')

CLUSTERING_PATH = os.path.join(
    OUTPUT_PATH,
    'clustering')
