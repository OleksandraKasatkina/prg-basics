###
# Returns the name of the day of the week for a given day number (1-Monday ... 7-Sunday)
#
def weekday(n):
      weekdays = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday", "Sunday"]
      return weekdays[n-1]

day_numbers = [1, 4, 7]
for day in day_numbers:
      print(f'Day {day}: {weekday(day)}')