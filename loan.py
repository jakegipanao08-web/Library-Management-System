# Loan class for Library Management System
from datetime import datetime

class Loan:
    """Represents a loan transaction (borrowing of a book)."""
    
    def __init__(self, loan_id, book, member):
        """Initialize a Loan object.
        
        Args:
            loan_id (str): Unique identifier for the loan
            book (Book): Book object being borrowed
            member (Member): Member object borrowing the book
        """
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.borrow_date = datetime.now()
        self.return_date = None
        self.is_active = True
    
    def close_loan(self):
        """Close the loan when the book is returned."""
        self.return_date = datetime.now()
        self.is_active = False
    
    def __str__(self):
        """String representation of the loan."""
        status = "Active" if self.is_active else "Closed"
        return f"{self.loan_id} - {self.member.name} borrowed {self.book.title} [{status}]"
    
    def __repr__(self):
        return f"Loan({self.loan_id}, {self.book.book_id}, {self.member.member_id}, active={self.is_active})"
