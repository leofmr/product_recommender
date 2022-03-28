import pandas as pd


# função auxiliar do modelo de classificação
def select_txt(X: pd.DataFrame, col: str) -> pd.Series:
    """Função de seleção de série para ser usada pelo pipeline de classificação

    Args:
        X (pd.DataFrame): dataframe com todos os dados
        col (str): coluna a ser selecionada

    Returns:
        pd.Series: série de dados selecionada
    """    
    return X[col]
    
# função auxiliar do modelo de classificação
def select_base_features(X: pd.DataFrame,
                         cols: list[str] = ["price", "weight", 
                                            "minimum_quantity"]
                         ) -> pd.DataFrame:
    """Função de seleção das variáveis para ser usada pelo pipeliene de
    classificação

    Args:
        X (pd.DataFrame): dataframe com todos os dados
        cols (list[str]): colunas a serem selecionadas

    Returns:
        pd.DataFrame: subset selecionado
    """    
    return X[cols]
