import json
import sqlite3

# Load the data
with open('database.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create a new table
try:
    c.execute('''
        CREATE TABLE lego_parts (
            SetNumber TEXT,
            PartID TEXT,
            Quantity INTEGER,
            Colour TEXT,
            Category TEXT,
            DesignID TEXT,
            PartName TEXT,
            ImageURL TEXT,
            SetCount INTEGER
        )
    ''')
except Exception as e:
    print(f"Error creating table: {e}")

# Insert each entry from the JSON data into the table
for entry in data:
    c.execute('''
        INSERT INTO lego_parts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        entry['SetNumber'],
        entry['PartID'],
        entry['Quantity'],
        entry['Colour'],
        entry['Category'],
        entry['DesignID'],
        entry['PartName'],
        entry['ImageURL'],
        entry['SetCount']
    ))

# Commit the changes and close the connection
conn.commit()
conn.close()