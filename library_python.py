class BookNode:
    """Node representing a single book in the Linked List."""
    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.is_issued = False
        self.issued_to = None
        self.next = None

class LibraryManagementSystem:
    """Library System combining Linked List and Hash Map for O(1) search."""
    def __init__(self):
        self.head = None
        self.book_lookup = {}  # Hash map to store references for fast search

    def add_book(self, book_id, title, author, category):
        if book_id in self.book_lookup:
            print(f"\n[Error] Book ID '{book_id}' already exists!")
            return
        
        # Create new node
        new_book = BookNode(book_id, title, author, category)
        
        # Insert at the beginning of Linked List (O(1) insertion)
        new_book.next = self.head
        self.head = new_book
        
        # Store in hash map for quick lookup
        self.book_lookup[book_id] = new_book
        print(f"\n[Success] Book '{title}' added successfully!")

    def search_book_by_id(self, book_id):
        """Searching using Hash Map - Time Complexity: O(1)"""
        if book_id in self.book_lookup:
            book = self.book_lookup[book_id]
            status = f"Issued to {book.issued_to}" if book.is_issued else "Available"
            print("\n--- Book Found ---")
            print(f"ID       : {book.book_id}")
            print(f"Title    : {book.title}")
            print(f"Author   : {book.author}")
            print(f"Category : {book.category}")
            print(f"Status   : {status}")
        else:
            print(f"\n[Not Found] Book with ID '{book_id}' does not exist.")

    def search_book_by_title(self, title):
        """Linear search through Linked List by title - Time Complexity: O(N)"""
        current = self.head
        found = False
        print(f"\n--- Search Results for Title: '{title}' ---")
        while current:
            if title.lower() in current.title.lower():
                status = f"Issued to {current.issued_to}" if current.is_issued else "Available"
                print(f"ID: {current.book_id} | Title: {current.title} | Author: {current.author} | Status: {status}")
                found = True
            current = current.next
        if not found:
            print("No matching books found.")

    def issue_book(self, book_id, student_name):
        if book_id in self.book_lookup:
            book = self.book_lookup[book_id]
            if book.is_issued:
                print(f"\n[Notice] Book '{book.title}' is already issued to {book.issued_to}.")
            else:
                book.is_issued = True
                book.issued_to = student_name
                print(f"\n[Success] Book '{book.title}' successfully issued to {student_name}.")
        else:
            print(f"\n[Not Found] Book ID '{book_id}' not found.")

    def return_book(self, book_id):
        if book_id in self.book_lookup:
            book = self.book_lookup[book_id]
            if not book.is_issued:
                print(f"\n[Notice] Book '{book.title}' was not currently issued.")
            else:
                print(f"\n[Success] Book '{book.title}' returned by {book.issued_to}.")
                book.is_issued = False
                book.issued_to = None
        else:
            print(f"\n[Not Found] Book ID '{book_id}' not found.")

    def display_all_books(self):
        """Traverse the Linked List to display all records - Time Complexity: O(N)"""
        current = self.head
        if not current:
            print("\n[Library] The library is currently empty.")
            return
        
        print("\n================== ALL LIBRARY BOOKS ==================")
        print(f"{'ID':<10} | {'Title':<20} | {'Author':<15} | {'Status':<15}")
        print("-" * 65)
        while current:
            status = f"Issued ({current.issued_to})" if current.is_issued else "Available"
            print(f"{current.book_id:<10} | {current.title:<20} | {current.author:<15} | {status:<15}")
            current = current.next
        print("=======================================================")


# --- Interactive Menu System ---
def main():
    library = LibraryManagementSystem()

    # Pre-loading some sample data for demonstration
    library.add_book("B101", "Data Structures", "Narasimha Karumanchi", "Computer Science")
    library.add_book("B102", "Python Crash Course", "Eric Matthes", "Programming")
    library.add_book("B103", "Digital Logic", "Morris Mano", "Electronics")

    while True:
        print("\n*** LIBRARY MANAGEMENT SYSTEM (DSA PROJECT) ***")
        print("1. Add New Book")
        print("2. Search Book by ID (Using Hash Map)")
        print("3. Search Book by Title (Using Linked List)")
        print("4. Issue Book to Student")
        print("5. Return Book")
        print("6. Display All Books")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == '1':
            b_id = input("Enter Book ID: ").strip()
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            category = input("Enter Category: ").strip()
            library.add_book(b_id, title, author, category)
            
        elif choice == '2':
            b_id = input("Enter Book ID to search: ").strip()
            library.search_book_by_id(b_id)
            
        elif choice == '3':
            title = input("Enter Book Title keyword to search: ").strip()
            library.search_book_by_title(title)
            
        elif choice == '4':
            b_id = input("Enter Book ID to issue: ").strip()
            student = input("Enter Student Name: ").strip()
            library.issue_book(b_id, student)
            
        elif choice == '5':
            b_id = input("Enter Book ID being returned: ").strip()
            library.return_book(b_id)
            
        elif choice == '6':
            library.display_all_books()
            
        elif choice == '7':
            print("\nExiting program. Good luck with your project presentation!")
            break
        else:
            print("\n[Error] Invalid choice! Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
