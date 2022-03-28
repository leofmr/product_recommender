from typing import Any
from scipy import stats
import pandas as pd

def series_mode(serie: pd.Series) -> Any:
    """Retorna a moda de uma série

    Args:
        serie (pd.Series): série de dados

    Returns:
        Any: item mais frequente da série
    """    
    return stats.mode(serie)[0][0]

def remove_duplicates(df: pd.DataFrame,
                      id_group: list[str] = "product_id",
                      mean_cols: list[str] = ["price", "weight",
                                             "minimum_quantity"],
                      mode_cols: list[str] = ["title",
                                              "concatenated_tags"]
                      ) -> pd.DataFrame:
    """Remoção de dados duplicados a partir de combinação de group. Utiliza
    mean_cols e mode_cols para unificar os registros em média e moda das
    observações duplicadas

    Args:
        data (pd.DataFrame): dataset
        group (list[str]): grupo que identifica unificamente o registro
        mean_cols (list[str]): variáveis a serem unificadas pela média
        mode_cols (list[str]): variáveis a serem unificadas pela moda

    Returns:
        pd.DataFrame: dataset sem registros duplicados
    """    
    duplicated_mask = df[id_group].duplicated(keep=False)
    
    dupli_data = df.loc[duplicated_mask]
    mode_stats = {col: series_mode for col in mode_cols}
    mean_stats = {col: "mean" for col in mean_cols}
    agg_stats = dict(**mode_stats, **mean_stats)
    unified_dupli_data = (dupli_data.
                          groupby(id_group, as_index=False).
                          agg(agg_stats))
    
    no_duplit_data = df.loc[~duplicated_mask]
    return pd.concat([no_duplit_data, unified_dupli_data]).set_index(id_group)