1. Extract → Transform → Load (ETL)

Extract: Load raw movie + rating data (CSV files from MovieLens dataset
).

Transform: Clean data, calculate average ratings, join with movie info.

Load: Save results into SQLite database (movies.db) for querying.

2. Database (SQLite)

Tables:

ratings → userId, movieId, rating

movies → movieId, title, genres

top_movies → top movies by avg rating

Stored inside db/movies.db.

Queried using sqlite3 or directly from VS Code (SQLite Explorer).

3. Machine Learning Model (scikit-learn)

Input: ratings.csv (userId, movieId, rating).

Build a User-Item Matrix (rows = users, cols = movies).

Train Matrix Factorization (TruncatedSVD) to learn user/movie embeddings.

Predict personalized ratings for each user.

Save model with joblib into models/recommender.pkl.

4. Querying

query.py → SQL-based queries from movies.db.

Example: Get top 10 movies overall by avg rating.

5. Tkinter GUI

GUI app (app.py) with 2 features:

Top 10 Movies Overall → fetched from SQLite.

Personalized Recommendations → predicted with ML model.