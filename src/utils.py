import pandas as pd
import argparse
import ast

def load_data():
    """Carrega os dados"""
    df = pd.concat([
        pd.read_pickle("data/train_query.pickle"),
        pd.read_pickle("data/test_query.pickle")
    ])
    return df

def load_args() -> pd.DataFrame:
    """Função de carregamento de configurações.

    Returns:
        pd.DataFrame: resultado a ser categorizado.
    """
    # criando os atributos que vão ser recebidos e parseando-os
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--category",
                        help="Texto de registro a ser categorizado",
                        type=str)
    parser.add_argument("-r",
                        "--recommendation",
                        help="Sistema de recomendação de produtos",
                        type=str)
    args = parser.parse_args()
    
    # extraindo dos atributos recebidos o registro a ser categorizado
    # e adequando-o para a predição
    if args.category is not None:
        product_dict = ast.literal_eval(args.category)
        product_df = pd.Series(product_dict).to_frame().T
    else:
        product_df = None
    
    return product_df, args.recommendation