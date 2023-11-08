import json
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
  host=os.getenv("DB_HOST"),
  user=os.getenv("DB_USER"),
  password=os.getenv("DB_PASSWORD"),
  database=os.getenv("DB_NAME")
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