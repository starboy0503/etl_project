import sqlite3  
import pandas as pd

def query_top_movies(limit=100):
    conn=sqlite3.connect("db/movies.db")
    query=f"Select title,avg_rating from top_movies order by avg_rating desc limit {limit};"

    df=pd.read_sql(query,conn)
    conn.close()
    return df 


def recommend_for_user(user_id,limit=5):
    conn=sqlite3.connect("db/movies.db")
    query=f"""Select r.userID,m.title,r.rating
    From ratings r
    join movies m on r.movieId=m.movieId
    where r.userId={user_id}
    order by r.rating desc
    Limit {limit};"""
    df=pd.read_sql(query,conn)
    conn.close()
    return df




if __name__=="__main__":
    result=query_top_movies(10)
    print("Top Movies:")
    print(result)   