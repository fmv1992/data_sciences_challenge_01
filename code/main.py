"""Execute the Code Challenge by Easynvest."""
import pandas as pd

from data_utilities import pandas_utilities as pu

import control
import exploratory_analysis


def main():
    """Main function for Code Challenge by Easynvest."""
    # Load the data.
    df_dados = pd.read_csv(control.DADOS_PATH,
                           encoding='latin1',
                           parse_dates=['DATA_NASCIMENTO'])
    df_depara = pd.read_csv(control.DEPARA_PATH,
                            encoding='latin1',
                            parse_dates=True)


    # Round to day as hour of birth may be considered unnecessary.
    df_dados['DATA_NASCIMENTO'] = df_dados['DATA_NASCIMENTO'].astype('int64')
    # Create an age variable
    # TODO


    # Uniformize the data.
    df_dados = pu.object_columns_to_category(df_dados)
    df_depara = pu.object_columns_to_category(df_depara)

    # Generate the exploratory analyses.
    exploratory_analysis.main(df_dados)




if __name__ == '__main__':
    main()
