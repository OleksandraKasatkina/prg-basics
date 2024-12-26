class EBook:
    def __init__(self, title, author, number_of_pages):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.current_page_number = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True
        self.current_page = 1
    
    def close_book(self):
        self.is_open = False

    def display_status(self):
        # Display the current status of the book
        if self.is_open:
            print(f"Book: {self.title}")
            print(f"Author: {self.author}")
            print(f"Total pages: {self.number_of_pages}")
            print(f"Current page: {self.current_page}")
        else:
            print(f"The book '{self.title}' is closed.")

    def next_page(self):
        # Go to the next page if the book is open and there are more pages
        if self.is_open:
            if self.current_page < self.number_of_pages:
                self.current_page += 1
            else:
                print("You are already on the last page.")
        else:
            print("The book is closed. You need to open it first.")

    def previous_page(self):
        # Go to the previous page if the book is open and we are not on the first page
        if self.is_open:
            if self.current_page > 1:
                self.current_page -= 1
            else:
                print("You are already on the first page.")
        else:
            print("The book is closed. You need to open it first.")
