import sqlite3

def load_to_sqlite(df,db_path="../db/sales.db"):
    conn=sqlite3.connect(db_path)
    df.to_sql('sales',conn,if_exists='append',index=False)
    conn.close()