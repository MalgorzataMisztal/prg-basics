from ebook import book

book1 = book("Python Basics", "John Smith", 120)
book1.open_book()
book1.display_status()

book1.next_page()
book1.next_page()
book1.next_page()
book1.next_page()
book1.display_status()

book1.close_book()

book1.next_page()
book1.previous_page()