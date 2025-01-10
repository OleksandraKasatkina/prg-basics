grades = [37,51,44,23,78,92,39,84,83,51]

def min_pts(limit):
   return lambda pts: pts>=limit

min_70 = list(filter(min_pts(70), grades))
min_40 = list(filter(min_pts(40), grades))
min_30 = list(filter(min_pts(30), grades))

print("Min 70 pts:", min_70)
print("Min 40 pts:", min_40)
print("Min 30 pts:", min_30)