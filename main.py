#!/usr/bin/env python3
# Main program for Library Management System
from library_service import LibraryService
from exceptions import BookNotFoundError, MemberNotFoundError, BookUnavailableError, LoanNotFoundError


def display_menu():
    """Display the main menu."""
    print("\n" + "="*50)
    print("         LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)


def add_book(service):
    """Handle adding a new book."""
    print("\n--- Add Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        if not book_id or not title or not author:
            print("✗ All fields are required!")
            return
        
        result = service.add_book(book_id, title, author)
        print(result)
    except Exception as e:
        print(f"✗ Error: {e}")


def register_member(service):
    """Handle registering a new member."""
    print("\n--- Register Member ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        if not member_id or not name or not email:
            print("✗ All fields are required!")
            return
        
        result = service.register_member(member_id, name, email)
        print(result)
    except Exception as e:
        print(f"✗ Error: {e}")


def borrow_book(service):
    """Handle borrowing a book."""
    print("\n--- Borrow Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not book_id or not member_id:
            print("✗ Both fields are required!")
            return
        
        result = service.borrow_book(book_id, member_id)
        print(result)
    except (BookNotFoundError, MemberNotFoundError, BookUnavailableError) as e:
        print(str(e))
    except Exception as e:
        print(f"✗ Error: {e}")


def return_book(service):
    """Handle returning a book."""
    print("\n--- Return Book ---")
    try:
        loan_id = input("Enter Loan ID: ").strip()
        
        if not loan_id:
            print("✗ Loan ID is required!")
            return
        
        result = service.return_book(loan_id)
        print(result)
    except (LoanNotFoundError, Exception) as e:
        print(str(e))


def view_books(service):
    """Display all books."""
    print("\n--- View Books ---")
    books = service.view_books()
    
    if not books:
        print("✗ No books found.")
        return
    
    print("\nBooks:")
    for book in books:
        print(f"  {book}")


def view_members(service):
    """Display all members."""
    print("\n--- View Members ---")
    members = service.view_members()
    
    if not members:
        print("✗ No members found.")
        return
    
    print("\nMembers:")
    for member in members:
        print(f"  {member}")


def view_loans(service):
    """Display all loans."""
    print("\n--- View Loans ---")
    loans = service.view_loans()
    
    if not loans:
        print("✗ No loans found.")
        return
    
    print("\nLoans:")
    for loan in loans:
        print(f"  {loan}")


def load_sample_data(service):
    """Load sample data for testing."""
    # Add sample books
    service.add_book("B001", "The Great Gatsby", "F. Scott Fitzgerald")
    service.add_book("B002", "To Kill a Mockingbird", "Harper Lee")
    service.add_book("B003", "1984", "George Orwell")
    service.add_book("B004", "Pride and Prejudice", "Jane Austen")
    service.add_book("B005", "The Catcher in the Rye", "J.D. Salinger")
    
    # Add sample members
    service.register_member("M001", "Alice Johnson", "alice@example.com")
    service.register_member("M002", "Bob Smith", "bob@example.com")
    service.register_member("M003", "Carol White", "carol@example.com")


def main():
    """Main program loop."""
    service = LibraryService()
    
    # Load sample data
    load_sample_data(service)
    print("\n✓ Sample data loaded successfully!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()
        
        if choice == "1":
            add_book(service)
        elif choice == "2":
            register_member(service)
        elif choice == "3":
            borrow_book(service)
        elif choice == "4":
            return_book(service)
        elif choice == "5":
            view_books(service)
        elif choice == "6":
            view_members(service)
        elif choice == "7":
            view_loans(service)
        elif choice == "8":
            print("\n✓ Program closed.")
            print("Thank you for using Library Management System!")
            break
        else:
            print("✗ Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
