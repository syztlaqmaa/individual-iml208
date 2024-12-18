#onlinebookshopsystem

import re

# Function to validate the email format
def validate_email(email):
    # Regular expression for basic email validation
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_regex, email):
        return True
    else:
        return False

# Function to validate phone number format (basic validation for length and digits)
def validate_phone_number(phone):
    if phone.isdigit() and len(phone) == 10:
        return True
    else:
        return False

# Prompt user for details
def get_user_data():
    print("Please enter the following details:")
    
    # Getting Name
    name = input("Enter your name: ").strip()
    
    # Getting and validating phone number
    phone = input("Enter your phone number (10 digits): ").strip()
    while not validate_phone_number(phone):
        print("Invalid phone number. Please enter a 10-digit number.")
        phone = input("Enter your phone number (10 digits): ").strip()

    # Getting and validating email
    email = input("Enter your email address: ").strip()
    while not validate_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email address: ").strip()

    # Display entered details
    print("\nThank you for entering your details!")
    print(f"Name: {name}")
    print(f"Phone Number: {phone}")
    print(f"Email Address: {email}")

# Call the function to prompt user for input
get_user_data()

#bookscart
def display_books(books):
    """Display all the books in the list."""
    if len(books) == 0:
        print("No books available.")
        return
    print("\nList of Books:")
    for idx, book in enumerate(books, start=1):
        print(f"{idx}. Title: {book['title']}, Author: {book['author']}, Price: ${book['price']:.2f}")

def add_book(books):
    """Prompt the user to add a new book."""
    print("\nEnter the details of the new book:")
    
    # Get book information from user input
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    
    # Validate and get the year of publication
    while True:
        try:
            year = int(input("Year of publication: ").strip())
            if year > 0:
                break
            else:
                print("Please enter a valid positive number for the year.")
        except ValueError:
            print("Invalid input. Please enter a valid year.")
    
    genre = input("Genre: ").strip()

    # Validate and get the price of the book
    while True:
        try:
            price = float(input("Price: $").strip())
            if price >= 0:
                break
            else:
                print("Price cannot be negative. Please enter a valid price.")
        except ValueError:
            print("Invalid input. Please enter a valid price (e.g., 19.99).")
    
    # Create a dictionary to represent the book and append it to the list
    book = {
        'title': title,
        'author': author,
        'year': year,
        'genre': genre,
        'price': price
    }
    books.append(book)
    print(f"\nBook '{title}' added successfully!")

    # Function to delete a book by title
def delete_book(books, title):
    # Try to find and remove the book by title
    for idx, book in enumerate(books):
        if book['title'].lower() == title.lower():
            del books[idx]
            print(f"Book '{title}' has been deleted.")
            return True
    print(f"No book found with the title '{title}'.")
    return False


def calculate_total_price(books):
    """Calculate the total price of all books."""
    total_price = sum(book['price'] for book in books)
    print(f"\nTotal price of all books: ${total_price:.2f}")
    return total_price

def process_payment(total_price):
    """Prompt the user for payment method and process payment."""
    print("\nChoose a payment method:")
    print("1. Credit Card")
    print("2. Cash")
    print("3. PayPal")

    payment_choice = input("Enter 1, 2, or 3: ").strip()

    if payment_choice == '1':
        # Credit Card Payment
        print(f"Processing Credit Card payment of ${total_price:.2f}...")
        print("Payment successful! Your books will be shipped to your address.")
    elif payment_choice == '2':
        # Cash Payment
        print(f"Processing Cash payment of ${total_price:.2f}...")
        print("Payment successful! Please pay the cash amount to the cashier.")
    elif payment_choice == '3':
        # PayPal Payment
        print(f"Processing PayPal payment of ${total_price:.2f}...")
        print("Payment successful! A receipt will be sent to your email.")
    else:
        # Invalid payment choice
        print("Invalid payment method. Please try again.")

def main():
    books = []  # List to store book data
    
    while True:
        print("\nBook Collection System")
        print("1. Add a new book")
        print("2. Display all books")
        print("3. Delete book")
        print("4. Calculate total price")
        print("5. Make a payment")
        print("6. Exit")
        
        choice = input("Choose an option (1, 2, 3, 4, 5,6): ").strip()
        
        if choice == '1':
            add_book(books)
        elif choice == '2':
            display_books(books)
        elif choice == "3":
            title_to_delete = input("Enter the title of the book to delete: ")
            delete_book(books, title_to_delete)
        elif choice == '4':
            total_price = calculate_total_price(books)
        elif choice == '5':
            if len(books) == 0:
                print("No books to process payment for. Please add books first.")
            else:
                total_price = calculate_total_price(books)
                process_payment(total_price)
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")

# Run the main function
if __name__ == "__main__":
    main()

