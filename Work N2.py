
class Book:
    def __init__(self, title, author, publishing_year):
        self.title = title
        self.author = author
        self.pub_year = publishing_year


class BookManager:
    book_list = []
    def add_new_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the book author: ")
        publishing_year = input("Enter the publishing year of the book: ")
        new_book = Book(title, author, publishing_year)
        self.book_list.append(new_book)

    def show_book_list(self):
        if len(self.book_list) == 0:
            print("Sorry, there are no books in the book manager yet...")
        else:
            print("Here is the list of the books you've added: ")
            for book in self.book_list:
                print(f"Title: {book.title}\nAuthor: {book.author}\nPublishing Year: {book.pub_year}\n---------------")

    def find_book_by_title(self):
        title = input("Enter which book you're looking for: ")
        found = False

        for book in self.book_list:
            if book.title.lower() == title.lower():
                print("Let me see... Ah, here it is!")
                print(f"Title: {book.title}\nAuthor: {book.author}\nPublishing Year: {book.pub_year}")

        if not found:
            print("I don't think I have that book, sorry...")


class Commands:

    def __init__(self):
        self.commands = {1: "Add a new book", 2: "Show the book list", 3: "Find a specific book", 4: "Arrivederci, Hasta luego, Ciao"}

    def get_command_dict(self):
        return self.commands

class UserInterface:

    def intro(self):
        print("Enter the desired number: ")

        commands = Commands()
        book_command = commands.get_command_dict()

        for key in book_command:
            print(f"{key}: {book_command[key]}")

    def user_add_book(self):
        title = input("Enter the book title: ")
        author = input("Enter the author: ")
        year = int(input("Enter the publishing year: "))

        book_manager.add_new_book(title, author, year)
        print("The book has been added!")



book_manager = BookManager()
book_manager.add_new_book()
