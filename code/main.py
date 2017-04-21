"""Execute the Code Challenge by Easynvest."""
import pandas as pd

from data_utilities import pandas_utilities as pu

import clustering
import control
import exploratory_analysis
import interpretation


def main():
    """Main function for Code Challenge by Easynvest."""
    # Load the data.
    df_dados = pd.read_csv(control.DADOS_PATH,
                           encoding='latin1',
                           parse_dates=['DATA_NASCIMENTO'])
    df_depara = pd.read_csv(control.DEPARA_PATH,
                            encoding='latin1',
                            parse_dates=True)

    # Uniformize the data.
    df_dados = pu.object_columns_to_category(df_dados)
    df_depara = pu.object_columns_to_category(df_depara)
    df_dados.columns = df_dados.columns.str.lower()

    # Uniformize the data.
    for obj_column in filter(lambda x: df_dados[x].dtype.name == 'category',
                             df_dados.columns):
        df_dados[obj_column] = df_dados[obj_column].str.lower().astype(
            'category')

    # Round to day as hour of birth may be considered unnecessary.
    df_dados['data_nascimento_int'] = df_dados['data_nascimento'].astype(
        'int64')
    # Create an age variable
    # Assume the dataset is from 2017/01/01.
    creation_date = pd.Timestamp(year=2017, day=1, month=1)
    age = (
        (creation_date - df_dados['data_nascimento'])
        / pd.Timedelta(days=365.25))
    # Round age to nearest int. Actually this distorts the data a little bit.
    # It is better to leave as float.
    # df_dados['age'] = np.rint(age)
    df_dados['age'] = age

    # Generate the exploratory analyses.
    exploratory_analysis.main(df_dados.drop('data_nascimento', axis=1))

    # For simplicity lets split 'ESTADO CIVIL' in three groups.
    est_civil = df_dados.estado_civil
    is_solteiro = est_civil.str.contains('solteir')
    is_casado = est_civil.str.contains('casad')
    is_outro = (~ (is_solteiro | is_casado))
    df_dados = df_dados.drop('estado_civil', axis=1)
    df_dados['estado_civil' + '_' + 'solteiro'] = is_solteiro
    df_dados['estado_civil' + '_' + 'casado'] = is_casado
    df_dados['estado_civil' + '_' + 'outro'] = is_outro

    # Map 'genero' to two groups as well.
    genero = df_dados.genero
    is_male = genero.str.contains('m')
    is_female = genero.str.contains('f')
    df_dados['genero' + '_' + 'm'] = is_male
    df_dados['genero' + '_' + 'f'] = is_female

    # Map 'perfil' to binary but do not drop it (it may be already a cluster).
    for one_perfil in df_dados.perfil.unique():
        df_dados['perfil_' + one_perfil] = df_dados.perfil == one_perfil

    # In this case since there are a lot of professions but not too many time,
    # I have decided not to transform 'profissao' into binary variables. If I
    # had to to do it I would create some 5 groups (is_analista, is_militar,
    # etc) of the most significant groups and the transform it into binary
    # variables the same way I just did with 'estado civil'.

    # Subset the data for clustering.
    df_clust = df_dados.drop(
        ['id', 'geo_referencia', 'data_nascimento', 'profissao', 'genero',
         'perfil', 'data_nascimento_int', ], axis=1).copy(True)

    # Uniformize the data for clustering.
    df_clust_scaled = clustering.preprocess_data(df_clust)

    # Select the number of clusters.
    all_cluster_labels = clustering.get_n_clusters(df_clust_scaled)
    # After carefull consideration I have decided that the adequate number of
    # clusters in this situations is 6.
    n_clusters = 6
    cluster_labels = all_cluster_labels[n_clusters]
    del all_cluster_labels

    # Interpret cluster data.
    df_dados['cluster'] = cluster_labels
    del cluster_labels
    interpretation.describe_clusters(df_dados)

    return None

if __name__ == '__main__':
    main()
