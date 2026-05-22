# Custom Exceptions for Library Management System

class BookNotFoundError(Exception):
    """Raised when a book is not found in the library."""
    pass


class MemberNotFoundError(Exception):
    """Raised when a member is not found in the library."""
    pass


class BookUnavailableError(Exception):
    """Raised when a book is not available for borrowing."""
    pass


class LoanNotFoundError(Exception):
    """Raised when a loan is not found."""
    pass
