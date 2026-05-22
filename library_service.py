# Library Service class - Core business logic for Library Management System
from book import Book
from member import Member
from loan import Loan
from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, LoanNotFoundError


class LibraryService:
    """Service class that manages all library operations."""
    
    def __init__(self):
        """Initialize the library service with empty dictionaries and lists."""
        self._books = {}        # Dictionary to store books: {book_id: Book}
        self._members = {}      # Dictionary to store members: {member_id: Member}
        self._loans = []        # List to store loans
        self._loan_counter = 0  # Counter for generating loan IDs
    
    # ================= BOOK OPERATIONS =================
    
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        """
        book = Book(book_id, title, author)
        self._books[book_id] = book
        return f"✓ Book added: {title}"
    
    def get_book(self, book_id):
        """Retrieve a book by its ID.
        
        Args:
            book_id (str): The book ID to retrieve
            
        Returns:
            Book: The book object
            
        Raises:
            BookNotFoundError: If book is not found
        """
        if book_id not in self._books:
            raise BookNotFoundError(f"✗ Book not found. (ID: {book_id})")
        return self._books[book_id]
    
    def view_books(self):
        """Get a list of all books in the library.
        
        Returns:
            list: List of Book objects
        """
        return list(self._books.values())
    
    # ================= MEMBER OPERATIONS =================
    
    def register_member(self, member_id, name, email):
        """Register a new member to the library.
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Name of the member
            email (str): Email address of the member
        """
        member = Member(member_id, name, email)
        self._members[member_id] = member
        return f"✓ Member registered: {name}"
    
    def get_member(self, member_id):
        """Retrieve a member by their ID.
        
        Args:
            member_id (str): The member ID to retrieve
            
        Returns:
            Member: The member object
            
        Raises:
            MemberNotFoundError: If member is not found
        """
        if member_id not in self._members:
            raise MemberNotFoundError(f"✗ Member not found. (ID: {member_id})")
        return self._members[member_id]
    
    def view_members(self):
        """Get a list of all members in the library.
        
        Returns:
            list: List of Member objects
        """
        return list(self._members.values())
    
    # ================= LOAN OPERATIONS =================
    
    def borrow_book(self, book_id, member_id):
        """Process a book borrowing request.
        
        Args:
            book_id (str): The book ID to borrow
            member_id (str): The member ID borrowing the book
            
        Returns:
            str: Success message
            
        Raises:
            BookNotFoundError: If book is not found
            MemberNotFoundError: If member is not found
            BookUnavailableError: If book is not available
        """
        # Get book and member (raises exceptions if not found)
        book = self.get_book(book_id)
        member = self.get_member(member_id)
        
        # Check if book is available
        if not book.available:
            raise BookUnavailableError(f"✗ Book is already borrowed. (Title: {book.title})")
        
        # Mark book as borrowed
        book.borrow()
        
        # Generate loan ID
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        
        # Create and store loan
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return f"✓ {member.name} borrowed {book.title}"
    
    def return_book(self, loan_id):
        """Process a book return.
        
        Args:
            loan_id (str): The loan ID to return
            
        Returns:
            str: Success message
            
        Raises:
            LoanNotFoundError: If loan is not found
        """
        loan = self.get_loan(loan_id)
        
        if not loan.is_active:
            raise Exception(f"✗ Loan {loan_id} is already closed.")
        
        # Return the book
        loan.book.return_book()
        loan.close_loan()
        
        return f"✓ {loan.member.name} returned {loan.book.title}"
    
    def get_loan(self, loan_id):
        """Retrieve a loan by its ID.
        
        Args:
            loan_id (str): The loan ID to retrieve
            
        Returns:
            Loan: The loan object
            
        Raises:
            LoanNotFoundError: If loan is not found
        """
        for loan in self._loans:
            if loan.loan_id == loan_id:
                return loan
        raise LoanNotFoundError(f"✗ Loan not found. (ID: {loan_id})")
    
    def view_loans(self):
        """Get a list of all loans.
        
        Returns:
            list: List of Loan objects
        """
        return list(self._loans)
