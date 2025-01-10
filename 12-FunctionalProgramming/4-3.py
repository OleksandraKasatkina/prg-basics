grades = [3.0, 5.0, 2.0, 3.5, 4.0, 4.0, 3.5, 2.0, 4.0, 2.0]

filtered_grades = list(filter(lambda grade: grade != 2.0, grades))

mean = sum(filtered_grades) / len(filtered_grades)

print(f"Arithmetic mean for grades <> 2.0 is {mean:.2f}")