###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.txt'

# Position
job_title = 'Software Engineer'

line_number = 1

with open('it_company.csv', 'r') as file:
   content = file.readlines()
   for line in content:
      if job_title in line:
         print(f'{line_number}. {line}', end='')
         line_number +=1