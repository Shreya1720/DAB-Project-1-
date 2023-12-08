from pathlib import Path
import sqlite3
import pandas as pd


#path = Pathlib.path().cwd() # use pathlib to get current working directory


def create_db(db_name, filename, table_name):
    file_path = Path('C:/Users/Shreya Thakkar/OneDrive/Desktop/SEM-1/INTRO TO PYTHON/Project/video_games.csv') # create a path to the data file

    con = sqlite3.connect('games.db',('autocommit'==False)) # create a connection to the database
    cursor = cursor = con.cursor() # create a cursor

    games = pd.read_csv(file_path)
    games.to_sql(table_name ,con ,  index = False , if_exists = 'replace')    # insert the data into the specified table 

    # execute a select statement as f-string and print results to verify insertion
    results = cursor.execute(f"SELECT * FROM {table_name}").fetchall()
    print(results)

    # commit the changes to the database
    con.commit()
    con.close() # close the connection


if __name__=="__main__":
    db_name = "games.db"
    filename = "video_games.csv"
    table_name = "game"
    create_db(db_name, filename, table_name)
