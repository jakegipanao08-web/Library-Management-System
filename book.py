# Book class for Library Management System

class Book:
    """Represents a book in the library."""
    
    def __init__(self, book_id, title, author):
        """Initialize a Book object.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        """
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True  # By default, books are available
    
    def borrow(self):
        """Mark the book as borrowed."""
        if not self.available:
            raise Exception(f"Book '{self.title}' is already borrowed.")
        self.available = False
    
    def return_book(self):
        """Mark the book as returned."""
        self.available = True
    
    def __str__(self):
        """String representation of the book."""
        status = "Available" if self.available else "Borrowed"
        return f"{self.book_id} - {self.title} by {self.author} [{status}]"
    
    def __repr__(self):
        return f"Book({self.book_id}, {self.title}, {self.author}, available={self.available})"
