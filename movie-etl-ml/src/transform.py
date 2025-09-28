import pandas as pd
from extract import extract_data

def transform_data():
    movies, ratings = extract_data()
    # Average ratings per movie
    avg_ratings = ratings.groupby("movieId")["rating"].mean().reset_index()
    avg_ratings.rename(columns={"rating": "avg_rating"}, inplace=True)
    # Merge with movie names
    top_movies = avg_ratings.merge(movies, on="movieId")
    return top_movies

if __name__ == "__main__":
    df = transform_data()
    print("✅ Data transformed. Sample:")
    print(df.head())
