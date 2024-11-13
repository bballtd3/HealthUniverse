import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Data for Breakfast, Lunch, and Dinner Menus with Image URLs
breakfast_data = {
    "Meal": [
        "Bacon, Egg And Cheese Muffin", "Fried Egg O’muffin Sandwich", "Scrambled Eggs", 
        "Bacon", "Fried Tater Tots", "Buttermilk Pancakes", "Everything Omelet", "Grits", 
        "Oatmeal", "Mango Banana Smoothie", "Strawberry Banana Smoothie", "Pineapple & Honey Smoothie", 
        "Mango Pineapple Smoothie", "Brown Sugar Cinnamon Mini Scone", "Strawberry Shortcake Muffins", 
        "Scrambled Tofu", "Lyonnaise Potatoes", "Roasted Red Beets"
    ],
    "Calories": [350, 310, 190, 70, 250, 180, 290, 90, 110, 100, 100, 190, 110, 200, 130, 60, 45, 25],
    "Total Fat (g)": [12, 10, 5, 6, 15, 9, 11, 0.5, 1, 0.5, 0.3, 1.5, 0.3, 10, 8, 3, 1, 0.2],
    "Protein (g)": [15, 13, 12, 5, 2, 4, 10, 2, 3, 1, 2, 4, 1, 3, 4, 2, 1, 1],
    "Image URL": [
        "https://example.com/bacon_egg_cheese.jpg", "https://example.com/fried_egg_muffin.jpg", 
        "https://example.com/scrambled_eggs.jpg", "https://example.com/bacon.jpg",
        "https://example.com/tater_tots.jpg", "https://example.com/pancakes.jpg",
        "https://example.com/omelet.jpg", "https://example.com/grits.jpg",
        "https://example.com/oatmeal.jpg", "https://example.com/mango_banana_smoothie.jpg",
        # Add URLs for all items...
    ],
}

# Convert data to DataFrames
breakfast_df = pd.DataFrame(breakfast_data)

# Displaying the food images
st.title("Personalized Nutrition and Meal Planning 🍴")

# Function to display meal images
def display_meal_images(df):
    for _, row in df.iterrows():
        st.image(row["Image URL"], caption=row["Meal"], use_column_width=True)
        st.write(f"Calories: {row['Calories']} kcal | Protein: {row['Protein (g)']} g | Total Fat: {row['Total Fat (g)']} g")

# Example for Breakfast Menu
st.header("Breakfast Menu")
display_meal_images(breakfast_df)

# Health Advisor Information
st.write("### Health Advisor Contacts")
st.write("For personalized dietary guidance, contact your college's health advisor:")
st.write("""
- **Bentley University**: Dr. Jane Doe, Nutrition Specialist - jane.doe@bentley.edu
- **Harvard University**: Dr. John Smith, Registered Dietitian - john.smith@harvard.edu
- **MIT**: Dr. Lisa White, Wellness Coordinator - lisa.white@mit.edu
""")

# The rest of the code remains unchanged
