import joblib
import pandas as pd

from src import utils, recommender_system
# essas funções são necessárias por conta do modelo
from src.clf_model import select_txt, select_base_features


def main():
    # carregando o modelo
    rf_clf_pipeline = joblib.load("assets/category_rf_clf_pipeline.joblib")
    # carregando o registro a ser categorizado
    product_df, query = utils.load_args()
    # fazendo a previsão da categoria
    if product_df is not None:
        product_category = rf_clf_pipeline.predict(product_df)[0]
        print(product_category)
    if query is not None:
        df = utils.load_data()
        prod_titles = pd.read_pickle(r"assets\prod_titles.pickle")
        recommender_system.main(query=query,
                                data=df,
                                prod_titles=prod_titles,
                                clf_pipeline=rf_clf_pipeline)
    

if __name__ == "__main__":
    main()