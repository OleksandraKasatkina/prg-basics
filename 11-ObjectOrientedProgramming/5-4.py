from ebook import EBook

def main():
    my_book = EBook("Python Programming", "John Doe", 150)

    print("Book status before opening:")
    my_book.display_status()
    
    print("\nOpening the book...")
    my_book.open_book()
    my_book.display_status()  

    print("\nReading a few pages...")
    my_book.next_page()
    my_book.next_page()
    my_book.display_status()

    print("\nTrying to go beyond the last page...")
    my_book.next_page()
    my_book.display_status()

    print("\nGoing back a few pages...")
    my_book.previous_page()
    my_book.previous_page()
    my_book.display_status()

    print("\nClosing the book...")
    my_book.close_book()
    my_book.display_status()

    print("\nTrying to read pages after closing the book...")
    my_book.next_page()
    my_book.previous_page()

if __name__ == "__main__":
    main()
