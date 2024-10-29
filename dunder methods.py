class Book:
    def __init__(self,title,author,num_pages):
        self.title=title
        self.author=author
        self.num_pages=num_pages
    def __str__(self):
        return f"{self.title}by {self.author} pages {self.num_pages}"
book1 = Book("The hobbit", "J.R.R. Tolkien",310)
book2 = Book("Harry Potter and the Philosopher's Stone","J.K. Rowling",223)
book3 = Book("The Lion, theWitch and the Wardrobe","C.S. Lewis",172)
print(book1)