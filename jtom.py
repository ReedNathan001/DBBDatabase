import json
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="G0dS3|\\ID_belady",
  database="hoobgloob"
)

cursor = db.cursor()

# Read the JSON file
with open('/Users/nathanreed/Desktop/database.json', 'r', encoding='utf-8-sig') as file:
  data = json.load(file)

# Loop through the data and insert each item into the database
for part in data:
  query = """
  INSERT INTO lego_parts (SetNumber, PartID, Quantity, Colour, Category, DesignID, PartName, ImageURL, SetCount) 
  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
  """
  values = (part['SetNumber'], part['PartID'], part['Quantity'], part['Colour'], part['Category'], part['DesignID'], part['PartName'], part['ImageURL'], part['SetCount'])
  cursor.execute(query, values)

# Commit the changes
db.commit()

print('Data imported successfully!')