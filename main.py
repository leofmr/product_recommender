import pandas as pd
import joblib
import argparse
import ast


def select_txt(X: pd.DataFrame, col: str):
    return X[col]
    

def select_base_features(X: pd.DataFrame):
    return X[["price", "weight", "minimum_quantity"]]

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
    args = parser.parse_args()
    
    # extraindo dos atributos recebidos o registro a ser categorizado
    # e adequando-o para a predição
    product_dict = ast.literal_eval(args.category)
    product_df = pd.Series(product_dict).to_frame().T
    
    return product_df

def main():
    # carregando o modelo
    rf_clf_pipeline = joblib.load("assets/category_rf_clf_pipeline.joblib")
    # carregando o registro a ser categorizado
    product_df = load_args()
    # fazendo a previsão da categoria
    product_category = rf_clf_pipeline.predict(product_df)[0]
    print(product_category)

if __name__ == "__main__":
    main()