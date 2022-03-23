import pandas as pd
import numpy as np
import joblib
import Levenshtein
import argparse
import ast
from scipy import stats

from src import nlp_preprocessing

def preprocess_txt(txt: str):
    """Executa preprocessamento textual padrão"""
    cleaned_txt = nlp_preprocessing.clean_text(txt)
    token_txt = nlp_preprocessing.custom_tokenizer(cleaned_txt)
    return " ".join(token_txt)

def get_top_docs(query, cleaned_doc_list, doc_titles, get_titles=True):
    """Gera as recomedações a partir de uma query e listas de referência"""
    cleaned_query = preprocess_txt(query)
    dists = [Levenshtein.distance(cleaned_query, doc)
             for doc in cleaned_doc_list]

    mask = np.array(dists).argsort()[:10]
    if get_titles:
        return doc_titles.iloc[mask].tolist()
    else:
        return doc_titles.iloc[mask].index.tolist()

def load_data():
    """Carrega os dados"""
    df = pd.concat([
        pd.read_pickle("data/train_query.pickle"),
        pd.read_pickle("data/test_query.pickle")
    ])
    return df


def series_mode(serie: pd.Series):
    """Calcula a moda de uma série"""
    return stats.mode(serie)[0][0]

def remove_duplicates(df, group="product_id",
                      num_cols=["price", "weight", "minimum_quantity"],
                      cat_cols=["title", "concatenated_tags"]) -> pd.DataFrame:
    """Função que remove os registros duplicados juntando os por média e moda
    a depender dos tipos de coluna"""
    mode_stats = {col: series_mode for col in cat_cols}
    mean_stats = {col: "mean" for col in num_cols}
    agg_stats = dict(**mode_stats, **mean_stats)
    return df.groupby(group).agg(agg_stats)

def make_predictions(query, clf_model):
    """Função que realiza as recomendações com predição de categoria
    majoritária"""
    df = load_data()
    prod_titles = (df[["product_id", "title"]].
                   drop_duplicates().set_index("product_id")["title"])
    cleaned_prod_titles = [preprocess_txt(txt) for txt in prod_titles]
    prod_id_select = get_top_docs(query,
                                  cleaned_prod_titles,
                                  prod_titles,
                                  False)
    selected_df = df.loc[df["product_id"].isin(prod_id_select)]
    selected_df = remove_duplicates(selected_df)
    predicted_cats = clf_model.predict(selected_df)
    major_cat = stats.mode(predicted_cats)[0][0]
    print(major_cat)
    for _id, title in selected_df["title"].iteritems():
        print(f"{_id} - {title}")
    
    

# função auxiliar do modelo de classificação
def select_txt(X: pd.DataFrame, col: str):
    return X[col]
    
# função auxiliar do modelo de classificação
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

def predict_single_category(df, clf_model):
    product_category = clf_model.predict(df)[0]
    print(product_category)

def main():
    # carregando o modelo
    rf_clf_pipeline = joblib.load("assets/category_rf_clf_pipeline.joblib")
    # carregando o registro a ser categorizado
    product_df, query = load_args()
    # fazendo a previsão da categoria
    if product_df is not None:
        predict_single_category(product_df, rf_clf_pipeline)
    if query is not None:
        make_predictions(query, rf_clf_pipeline)
    

if __name__ == "__main__":
    main()