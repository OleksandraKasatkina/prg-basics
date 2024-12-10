def calculate_file_stats(filename):
    """
    Calculate the number of lines, characters, and words in a file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Calculate number of lines
        num_lines = content.count('\n') + 1 if content else 0
        
        # Calculate number of characters
        num_characters = len(content)
        
        # Calculate number of words
        num_words = len(content.split())
        
        # Display results
        print(f"File name: {filename}")
        print(f"Number of lines: {num_lines}")
        print(f"Number of characters: {num_characters}")
        print(f"Number of words: {num_words}")
        
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. Please enter a valid file name.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main program
if __name__ == "__main__":
    filename = input("Enter the name of the file: ").strip()
    calculate_file_stats(filename)
