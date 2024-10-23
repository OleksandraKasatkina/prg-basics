###
# Program that calculates the employee's salary,
# taking into account the possibility of receiving a bonus.
#
basic_salary = 5000
total_salary = 0
bonus_amount = int(input('Enter the amount of the bonus in percentage: ')) 
bonus = bonus_amount / 100 
is_bonus = bonus > 0

if is_bonus == True:
    total_salary = basic_salary + (basic_salary * bonus)
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary} PLN')