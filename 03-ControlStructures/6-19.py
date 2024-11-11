### 
# A program that prints a survey consisting of three questions

print('SURVEY')
interested_in_cs = input('Are you interested in computer science? (y/n): ')
likes_gaming = input('Do you like playing computer games? (y/n): ')
has_instagram = input('Do you have an Instagram account? (y/n): ')

print('SURVEY RESULTS')
print('Interested in computer science:', 'Yes' if interested_in_cs == 'y' else 'No')
print('Playing computer games:', 'Yes' if likes_gaming == 'y' else 'No')
print('Has an Instagram account:', 'Yes' if has_instagram == 'y' else 'No')