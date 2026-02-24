import sqlite3
import os
from database import add_entry, init_db

# This ensures we find the EXACT same database the app uses
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "data", "journal.db")

print(f"Targeting database at: {DB_PATH}")

def seed_system():
    # 1. Initialize the table if it doesn't exist
    init_db()
    
    # 2. The 8 test entries
    test_data = [
        ("2026-02-11", 5, 7, 6.0, 4, "Better sleep but still feeling the pressure."),
        ("2026-02-12", 3, 9, 4.5, 2, "Rough night, very high stress levels."),
        ("2026-02-13", 6, 5, 7.5, 6, "Weekend approaching, stress decreasing."),
        ("2026-02-14", 8, 3, 8.5, 8, "Great rest, mood significantly improved."),
        ("2026-02-15", 9, 2, 9.0, 9, "Fully recovered and feeling vibrant."),
        ("2026-02-16", 7, 4, 7.0, 7, "Back to work, maintaining balance."),
        ("2026-02-17", 5, 6, 6.5, 5, "Mid-week slump, average metrics."),
    ]

    # 3. Inject data
    for entry in test_data:
        add_entry(*entry)
    
    print("Injection complete. Refresh your Streamlit app.")

if __name__ == "__main__":
    seed_system()