class Library:
    def __init__(self, library_name, *list_of_books):
        self.list_of_books = list(list_of_books)
        self.library_name = library_name
        self.lender_dict = {}
        print("Welcome to", self.library_name)

    def Displaybooks(self):
        print("Books available in the library: \n")
        for book in self.list_of_books:
            print(book)

    def LendBooks(self):
        def IssueBook():
            for key, value in self.lender_dict.items():
                if value == lender_name:
                    return False
            return True

        lender_name = input("Enter your name: ").lower()
        if IssueBook():
            bookToIssue = input("Enter the book name: ").lower()
            if bookToIssue in self.list_of_books:
                newItem = {bookToIssue: lender_name}
                self.lender_dict.update(newItem)
                self.list_of_books.remove(bookToIssue)
                print("Book issued successfully")
            else:
                print("Sorry no such book exists !")
        else:
            print("Sorry you cannot issue more than one book at a time")

    def Addbook(self):
        bookName = input("Enter the book name: \n")
        self.list_of_books.append(bookName)
        print("Book added successfully.")

    def Returnbook(self):
        booktoreturn = input("Enter the name of the book to return: \n").lower()
        if booktoreturn in self.lender_dict.keys():
            del self.lender_dict[booktoreturn]
            self.list_of_books.append(booktoreturn)
            print("Books returned successfully.")
        else:
            print("No such book is issued.")

    def printlenderlist(self):
        for key, value in self.lender_dict.items():
            print(f"{value} has issued {key}")

Books = Library("my library", "Goosebumbs", "Frankestein", "Lord of the Rings")

def main():
    while 1:
        choice = input(">> ").lower().replace(" ", "")
        if choice == "displaybook":
           Books.Displaybooks()
        elif choice == "lendbook":
            Books.LendBooks()
        elif choice == "addbook":
            Books.Addbook()
        elif choice == "returnbook":
            Books.Returnbook()
        elif choice == "printlenderlist":
            Books.printlenderlist()
        elif choice == "exit":
            break
        else:
            print("Not a valid command !")
    print("Library is closed now")

main()