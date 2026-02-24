import sqlite3
import pandas as pd
import os

# 1. Build an absolute path to the data folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FOLDER = os.path.join(BASE_DIR, "data")
DB_PATH = os.path.join(DB_FOLDER, "journal.db")

# 2. Ensure the data directory exists
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS entries
                 (date TEXT PRIMARY KEY, 
                  mood INTEGER, 
                  stress INTEGER, 
                  sleep REAL, 
                  energy INTEGER, 
                  note TEXT)''')
    conn.commit()
    conn.close()
    print(f"Database initialized at: {DB_PATH}") # Check your VS Code terminal for this!

def add_entry(date, mood, stress, sleep, energy, note):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT OR REPLACE INTO entries VALUES (?,?,?,?,?,?)", 
              (str(date), mood, stress, sleep, energy, note))
    conn.commit()
    conn.close()

def get_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM entries", conn)
    conn.close()
    if not df.empty:
        df['date'] = pd.to_datetime(df['date'])
    return df

# Initialize immediately
init_db()