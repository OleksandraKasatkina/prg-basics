import re

def filter_files_with_four_char_extensions(file_path):
    try:
        # Open and read the file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Regular expression to match file names with four-character extensions
        pattern = r'\.\w{4}$'
        
        # Filter and print file names
        print("Files with four-character extensions:")
        for line in lines:
            filename = line.strip()  # Remove any leading/trailing whitespace
            if re.search(pattern, filename):
                print(filename)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")

# Prompt the user to enter the file name
file_path = "files.txt"

# Call the function
filter_files_with_four_char_extensions(file_path)
