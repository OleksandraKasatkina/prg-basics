import csv

def filter_products(file_path):
    try:
        # Open the CSV file
        with open(file_path, mode="r", encoding="utf-8") as file:
            # Create a CSV reader object
            reader = csv.DictReader(file)
            
            # Print the header for the result
            print("PRODUCTS WITH PRICE < 60 AND STOCK < 40")
            print("=======================================")
            
            # Iterate over each row in the CSV file
            for row in reader:
                price = float(row["Price"])
                stock = int(row["Stock_Quantity"])
                
                # Check if the price is less than 60 and stock is less than 40
                if price < 60 and stock < 40:
                    # Print relevant product details
                    print(f"Product: {row['Product_Name']}, Category: {row['Category']}, Price: {price}, Stock: {stock}")
    except FileNotFoundError:
        print("The file does not exist. Please check the file path.")

# Main program
file_path = "clothing.csv"  # Path to the CSV file
filter_products(file_path)
