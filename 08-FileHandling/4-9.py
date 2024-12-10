import csv

def find_graphic_designers(file_path):
    try:
        # Open the CSV file
        with open(file_path, mode="r", encoding="utf-8") as file:
            # Create a CSV reader object
            reader = csv.DictReader(file)
            
            # Print the header for the result
            print("GRAPHIC DESIGNERS")
            print("=================")
            
            # Iterate over each row in the CSV file
            for row in reader:
                # Check if the job title is 'Graphic Designer'
                if row["Job Title"] == "Graphic Designer":
                    # Print first name, last name, and email
                    print(f"{row['First Name']} {row['Last Name']},{row['Email']}")
    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")

# Main program
file_path = "it_company.csv"  # Path to the CSV file
find_graphic_designers(file_path)
