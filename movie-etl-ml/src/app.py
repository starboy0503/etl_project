import tkinter as tk
from tkinter import messagebox
import pandas as pd
import sqlite3
import joblib
from recommend import recommend_for_user


class MovieRecommenderApp:
    def __init__(self,root):
        self.root=root
        self.root.title("Movie Recommender")
        self.root.geometry("650x500")

        tk.Label(root,text="Movie Recommender",font=("Helvetica",16,"bold") ).pack(pady=10)


        tk.Label(root,text="Enter User ID:").pack(pady=5)
        self.user_entry=tk.Entry(root)
        self.user_entry.pack(pady=5)

        tk.Button(root,text="Get Personalised Recommendations",command=self.get_recommendations).pack(pady=10)
        tk.Button(root,text="Show Top Movies",command=self.show_top_movies).pack(pady=10)

        self.output_box=tk.Text(root,height=20,width=80)
        self.output_box.pack(pady=10)

    def get_recommendations(self):
        try:
            user_id=int(self.user_entry.get())
            resc=recommend_for_user(user_id,top_n=5)
            
            self.output_box.delete(1.0,tk.END)
            if resc.empty:
                self.output_box.insert(tk.END,"No recommendations found for this user ID.\n")
            else:
                self.output_box.insert(tk.END,f"🎯 Personalized Recommendations for User {user_id}:\n\n")
                for _,row in resc.iterrows():
                    self.output_box.insert(tk.END,f"-{row['title']} (Predicted Rating: {row['pred_rating']:.2f}, Genres: {row['genres']})\n")
        except ValueError:
            messagebox.showerror("Invalid Input","Please enter a valid User ID.")
    

    def show_top_movies(self):
        try:
            conn=sqlite3.connect("db/movies.db")
            query=f"""
            SELECT TITLE, avg_rating
            FROM top_movies
            ORDER BY avg_rating DESC
            LIMIT 10;"""
            df=pd.read_sql(query,conn)
            conn.close()

            self.output_box.delete(1.0,tk.END)
            self.output_box.insert(tk.END,"🏆 Top 10 Movies by Average Rating:\n")

            for _,row in df.iterrows():
                self.output_box.insert(tk.END,f"-{row['title']} (Avg Rating: {row['avg_rating']:.2f})\n")
        except Exception as e:
            messagebox.showerror("Error",str(e))

if __name__=="__main__":
    root=tk.Tk()
    app=MovieRecommenderApp(root)
    root.mainloop()