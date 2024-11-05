import sqlite3

def initialize_db():
    conn = sqlite3.connect('chocolate_house.db')
    cursor = conn.cursor()
    
    # Create flavors table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS flavors (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            is_seasonal BOOLEAN NOT NULL
        )
    ''')
    
    # Create ingredients table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ingredients (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            stock INTEGER NOT NULL
        )
    ''')
    
    # Create suggestions table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS suggestions (
            id INTEGER PRIMARY KEY,
            flavor_suggestion TEXT NOT NULL,
            has_allergens BOOLEAN NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
