###
# A program that prints your height both in cm and in feet and inches.
#
cm = 164
cm_per_foot = 30.48
cm_per_inch = 2.54
feet = cm // cm_per_foot
remainder = cm % cm_per_foot
inches = remainder // cm_per_inch
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {int(feet)} feet and {int(inches)} inches')