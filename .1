import sqlite3
from datetime import datetime

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('dining_nutrition.db')
cursor = conn.cursor()

# Sample table creation (if not already created)
cursor.execute('''
CREATE TABLE IF NOT EXISTS nutrition_data (
    id INTEGER PRIMARY KEY,
    item_name TEXT,
    calories INTEGER,
    protein INTEGER,
    carbs INTEGER,
    fats INTEGER
)
''')

# Example of inserting sample data (replace with actual data from Sodexo)
sample_data = [
    ("Grilled Chicken Breast", 200, 35, 0, 5),
    ("Mashed Potatoes", 150, 3, 25, 4),
    ("Salad", 50, 2, 10, 0),
    # Add more items as needed
]
cursor.executemany("INSERT INTO nutrition_data (item_name, calories, protein, carbs, fats) VALUES (?, ?, ?, ?, ?)", sample_data)
conn.commit()

# Function to log what food a user selects
def log_food_consumption(user_id, item_name):
    current_date = datetime.now().strftime("%Y-%m-%d")
    cursor.execute("INSERT INTO user_food_log (user_id, date, item_name) VALUES (?, ?, ?)", (user_id, current_date, item_name))
    conn.commit()

# Function to calculate daily nutrition based on logged foods
def calculate_daily_nutrition(user_id, date):
    cursor.execute('''
        SELECT item_name, calories, protein, carbs, fats
        FROM nutrition_data
        WHERE item_name IN (SELECT item_name FROM user_food_log WHERE user_id = ? AND date = ?)
    ''', (user_id, date))
    
    daily_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    for item in cursor.fetchall():
        daily_nutrition["calories"] += item[1]
        daily_nutrition["protein"] += item[2]
        daily_nutrition["carbs"] += item[3]
        daily_nutrition["fats"] += item[4]
    
    return daily_nutrition

# Example usage
user_id = 123  # Replace with actual user ID
log_food_consumption(user_id, "Grilled Chicken Breast")
log_food_consumption(user_id, "Salad")

daily_intake = calculate_daily_nutrition(user_id, datetime.now().strftime("%Y-%m-%d"))
print("Today's intake:", daily_intake)

# Close the connection when done
conn.close()
