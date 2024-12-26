from statistics import Statistics  # Import the Statistics class from statistics.py

def main():
    stats_calculator = Statistics()
    
    numbers = [12, 37, 6, 9, 17]
    
    # Add numbers to the Statistics object
    for num in numbers:
        stats_calculator.add_number(num)
    
    stats_calculator.display_numbers()
    
    stats_calculator.print_statistics()

if __name__ == "__main__":
    main()
