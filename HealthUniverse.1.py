import streamlit as st
from datetime import datetime

# Sample data (Replace with actual Sodexo data)
sodexo_data = {
    "Grilled Chicken Breast": {"calories": 200, "protein": 35, "carbs": 0, "fats": 5},
    "Mashed Potatoes": {"calories": 150, "protein": 3, "carbs": 25, "fats": 4},
    "Salad": {"calories": 50, "protein": 2, "carbs": 10, "fats": 0},
    # Add more items as needed
}

# Initialize session state for food logging
if 'selected_food' not in st.session_state:
    st.session_state.selected_food = []

st.title("Bentley Dining Hall Nutrition Tracker")
st.write("Select the food items you consumed today:")

# List available food items with checkboxes
for food, nutrition in sodexo_data.items():
    if st.checkbox(food):
        if food not in st.session_state.selected_food:
            st.session_state.selected_food.append(food)
    else:
        if food in st.session_state.selected_food:
            st.session_state.selected_food.remove(food)

# Calculate daily nutrition intake
def calculate_daily_nutrition(selected_food):
    daily_nutrition = {"calories": 0, "protein": 0, "carbs": 0, "fats": 0}
    for item in selected_food:
        nutrition = sodexo_data[item]
        daily_nutrition["calories"] += nutrition["calories"]
        daily_nutrition["protein"] += nutrition["protein"]
        daily_nutrition["carbs"] += nutrition["carbs"]
        daily_nutrition["fats"] += nutrition["fats"]
    return daily_nutrition

# Display daily nutritional summary
if st.button("Calculate Daily Intake"):
    daily_intake = calculate_daily_nutrition(st.session_state.selected_food)
    st.subheader("Today's Nutritional Intake")
    st.write(f"Calories: {daily_intake['calories']} kcal")
    st.write(f"Protein: {daily_intake['protein']} g")
    st.write(f"Carbohydrates: {daily_intake['carbs']} g")
    st.write(f"Fats: {daily_intake['fats']} g")

# Optional: Reset selection
if st.button("Reset Selection"):
    st.session_state.selected_food = []

