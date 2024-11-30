# Weekly meal plan [Breakfast, Lunch, Dinner] for 7 days
meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

# Returns a week day name
def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]

# Returns a string with day meal names
# separated by comma
def day_meal_plan(meal_plan, day_number):
   day_meals = meal_plan[day_number - 1]
   result = day_meals[0]
   for meal in day_meals[1:]:
       result += ", " + meal
   return result

# Prints weekly meal plan
print("WEEKLY MEAL PLAN")
print("(Breakfast, Lunch, Dinner)")
print("==========================")
for i in range(1, 8):  # Days 1 to 7
    print(f"{weekday(i)}: {day_meal_plan(meal_plan, i)}")