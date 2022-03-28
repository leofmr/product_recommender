import Levenshtein
import pandas as pd
from . import nlp_preprocessing, preprocessing

def preprocess_title_data(data: pd.DataFrame) -> pd.DataFrame:
    prod_titles = (data[["product_id", "title"]].
                   drop_duplicates().
                   set_index("product_id"))
    prod_titles["cleaned_title"] = (prod_titles["title"].
                                    apply(nlp_preprocessing.preprocess_txt))
    
    return prod_titles

def get_top_prods(query: str,
                  prod_titles: pd.DataFrame,
                  get_titles: bool = True,
                  topn: int = 10) -> list:
    """Gera as recomedações a partir de uma query e listas de referência"""
    cleaned_query = nlp_preprocessing.preprocess_txt(query)
    data = prod_titles.copy()
    data["dist"] = (data["cleaned_title"].
                    apply(lambda x: Levenshtein.distance(x, cleaned_query)))
    selected_prods = data.sort_values("dist").head(topn)
    
    if get_titles:
        return selected_prods["title"].tolist()
    else:
        return selected_prods.index.tolist()
    

def main(query, data, clf_model):
    """Função que realiza as recomendações com predição de categoria
    majoritária"""
    prod_titles = preprocess_title_data(data=data)
    selected_ids = get_top_prods(query=query,
                                 prod_titles=prod_titles,
                                 get_titles=False)
    
    selected_df = data.loc[data["product_id"].isin(selected_ids)]
    selected_df = preprocessing.remove_duplicates(selected_df)
    predicted_cats = clf_model.predict(selected_df)
    major_cat = preprocessing.series_mode(predicted_cats)
    print(major_cat)
    for _id, title in selected_df["title"].iteritems():
        print(f"{_id} - {title}")