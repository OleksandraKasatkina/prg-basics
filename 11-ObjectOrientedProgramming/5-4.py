# main.py file
from ebook import EBook  # Importing the Ebook class from ebook.py

def main():
    # Create an Ebook instance with title, author, and number of pages
    my_book = EBook("Python Programming", "John Doe", 150)

    # Try reading the book when it is closed
    print("Book status before opening:")
    my_book.display_status()
    
    # Open the book
    print("\nOpening the book...")
    my_book.open_book()
    my_book.display_status()  # Show the status after opening the book

    # Read a few pages (go to next page)
    print("\nReading a few pages...")
    my_book.next_page()  # Go to next page
    my_book.next_page()  # Go to next page
    my_book.display_status()  # Display status after reading

    # Try to read more pages (check boundary conditions)
    print("\nTrying to go beyond the last page...")
    my_book.next_page()  # Go to next page beyond the last one
    my_book.display_status()

    # Read a few previous pages
    print("\nGoing back a few pages...")
    my_book.previous_page()  # Go to previous page
    my_book.previous_page()  # Go to previous page
    my_book.display_status()  # Display status after going back

    # Close the book
    print("\nClosing the book...")
    my_book.close_book()
    my_book.display_status()  # Display status after closing the book

    # Try to read pages after the book is closed
    print("\nTrying to read pages after closing the book...")
    my_book.next_page()  # Attempt to go to the next page while the book is closed
    my_book.previous_page()  # Attempt to go to the previous page while the book is closed

if __name__ == "__main__":
    main()
