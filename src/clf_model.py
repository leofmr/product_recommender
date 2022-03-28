import pandas as pd


# função auxiliar do modelo de classificação
def select_txt(X: pd.DataFrame, col: str):
    return X[col]
    
# função auxiliar do modelo de classificação
def select_base_features(X: pd.DataFrame):
    return X[["price", "weight", "minimum_quantity"]]
