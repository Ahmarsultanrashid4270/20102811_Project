import sqlite3

conn = sqlite3.connect("database.db")

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS animals (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     animal_id TEXT,
                    name TEXT,
                    species TEXT, 
                    breed TEXT,
                    age INTEGER,
                    gender TEXT,
                    status TEXT
               )

              """  )    

conn.commit()

conn.close()

print("Database created")
