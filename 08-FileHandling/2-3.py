###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, 'r') as original:
   content = original.read()

# write the content to the target file (copy)
with open(target_file, 'w') as target:
   target.write(content)

print(f"Contents of '{original_file}' have been copied to '{target_file}'.")