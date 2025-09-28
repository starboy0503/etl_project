import pandas as pd 
import numpy as np
from sklearn.decomposition import TruncatedSVD
import joblib


def train_recommender():
    ratings=pd.read_csv("/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/data/ratings.csv")
    movies=pd.read_csv("/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/data/movies.csv")

    rating_matrix=ratings.pivot(index="userId",columns="movieId",values="rating").fillna(0)
    svd=TruncatedSVD(n_components=20,random_state=42)
    latent_matrix=svd.fit_transform(rating_matrix)

    joblib.dump({
        "svd":svd,
        "rating_matrix":rating_matrix,
        "movies":movies,},"/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/models/recommender.pkl"
    )
    print("✅ Recommender model trained and saved to /Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/models/recommender.pkl")

def recommend_for_user(userId,top_n=5):
        model_data=joblib.load("/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/models/recommender.pkl")
        svd,rating_matrix,movies=model_data["svd"],model_data["rating_matrix"],model_data["movies"]

        if userId not in rating_matrix.index:
            return pd.DataFrame(column=["movieId","title"])
        
        user_idx=rating_matrix.index.get_loc(userId)
        user_vector=svd.transform([rating_matrix.iloc[user_idx]])[0]

        preds=np.dot(user_vector,svd.components_)
        pred_df=pd.DataFrame({
            "movieId":rating_matrix.columns,
            "pred_rating":preds
        })

        recs=pred_df.merge(movies,on="movieId").sort_values("pred_rating",ascending=False).head(top_n)
        return recs[["title","pred_rating","genres"]]
    
if __name__=="__main__":
    train_recommender()
    print(recommend_for_user(1,5))