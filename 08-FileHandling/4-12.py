import csv

def copy_books_by_genre(input_file, genre, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header
        outfile.write(f"{header[0]},{header[1]},{header[2]},{header[3]}\n")  # Write the header

        for row in reader:
            if row[2].strip().lower() == genre.lower():
                outfile.write(f"{row[0]},{row[1]},{row[2]},{row[3]}\n")  # Write matching rows

def main():
    input_file = 'books.csv'
    genre_to_file = {
        'Fantasy': 'books_fantasy.txt',
        'Historical': 'books_historical.txt',
        'Romance': 'books_romance.txt',
        'Classic': 'books_classic.txt',
    }
    
    for genre, output_file in genre_to_file.items():
        copy_books_by_genre(input_file, genre, output_file)

if __name__ == "__main__":
    main()
