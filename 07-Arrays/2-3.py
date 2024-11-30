# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

food_total = 0
transport_total = 0
utilities_total = 0
month_total = 0

for week in monthly_expenses:
    food_total += week[0]        
    transport_total += week[1]   
    utilities_total += week[2]   
    month_total += sum(week)    

# Calculate weekly totals
weekly_totals = [sum(week) for week in monthly_expenses]



# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:', food_total)
print('Transport:', transport_total)
print('Utilities:', utilities_total)
print('Week 1:', weekly_totals[0])
print('Week 2:', weekly_totals[1])
print('Week 3:', weekly_totals[2])
print('Week 4:', weekly_totals[3])
print('---------------')
print('TOTAL:', month_total)