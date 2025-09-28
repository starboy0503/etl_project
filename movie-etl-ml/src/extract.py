import pandas as pd

def extract_data():
    movies = pd.read_csv("/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/data/movies.csv")
    ratings = pd.read_csv("/Users/adityadhanrajsingh/Desktop/etl_projects/movie-etl-ml/data/ratings.csv")
    return movies, ratings

if __name__ == "__main__":
    m, r = extract_data()
    print("✅ Data extracted:", m.shape, r.shape)
    print(m.head())
    print(r.head())
