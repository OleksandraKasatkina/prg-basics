categories = ["Food", "Transport", "Rent", "Entertainment"]
expenses = [500, 150, 1000, 200]

max_expense = max(expenses)
max_index = expenses.index(max_expense)

the_most_expensive = categories[max_index]

print('The most expensive category:', the_most_expensive)