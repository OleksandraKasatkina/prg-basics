def save_powers(file_path):
    try:
        # Open the file in write mode
        with open(file_path, mode="w", encoding="utf-8") as file:
            # Write the header for the file
            file.write("Number,Square,Cube\n")
            
            # Iterate over numbers from 1 to 100
            for number in range(1, 101):
                square = number ** 2
                cube = number ** 3
                # Prepare the result string
                result = f"{number},{square},{cube}\n"
                # Print the result to the console
                print(result.strip())
                # Write the result to the file
                file.write(result)
        print(f"Results saved to {file_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main program
file_path = "powers.txt"  # Name of the text file to save results
save_powers(file_path)