def display_file_in_chunks(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            while True:
                # Read the next 5 lines
                lines = [file.readline().strip() for _ in range(5)]
                
                # Stop if no more lines are left
                if not any(lines):
                    print("End of file.")
                    break
                
                # Print the lines
                for line in lines:
                    if line:  # Print only non-empty lines
                        print(line)
                
                # Wait for Enter key to continue
                input("Press Enter key...")
    except FileNotFoundError:
        print(f"The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
if __name__ == "__main__":
    display_file_in_chunks("it_company.csv")