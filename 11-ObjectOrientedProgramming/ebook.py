class book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.c_page = 1
        self.is_open = False

    def open_book(self):
        self.is_open = True
        print("The book is now open.")

    def close_book(self):
        self.is_open = False
        print("The book is now closed.")

    def next_page(self):
        if not self.is_open:
            print("Cannot read pages. The book is closed.")
            return
        
        if self.c_page < self.pages:
            self.c_page += 1
        else:
            print("You are already on the last page.")
        
    def previous_page(self):
        if not self.is_open:
            print("Cannot read pages. The book is closed.")
            return

        if self.c_page > 1:
            self.c_page -= 1
        else:
            print("You are already on the first page.")

    def display_status(self):
        status = "open" if self.is_open else "closed"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Current page: {self.c_page}")
        print(f"Book status: {status}")
        print("-" * 30)