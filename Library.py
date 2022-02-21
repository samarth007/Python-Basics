class Libray():
    def __init__(self,list_of_books,name_of_library):
        self.list_of_books=list_of_books
        self.name_of_library=name_of_library
        self.lended_books=[]

    def display(self):
        for i in self.list_of_books:
            print(i)
        return "These books we have"

    def add_books(self,addBooks):
        self.list_of_books.append(addBooks)
        print('Book added : ',self.list_of_books)

    def lendBooks(self,book):
        if book in self.list_of_books:
            self.lended_books.append(book)
            print('Book lended : ',book)
            self.list_of_books.remove(book)
        elif book in self.lended_books:
            print("Books is already lended ")
        else:
            print("requested book is not available")


public=Libray(['cricket','Football','Hockey','Baseball','soccer'],'public_Library')
value=True

while value==True:
    user_name=input("Enter your name")
    user_input=eval(input(f'welcome {user_name} to {public.name_of_library}\n'
                         "Enter the options below :\n"
                          "1.To display books\n"
                           "2. To add books\n"
                           "3. To lend books\n"))
    if user_input==1:
        public.display()
    elif user_input==2:
        new_book=input("Enter the name of the book")
        public.add_books(new_book)
    elif user_input==3:
        book=input("Enter the book to be lend")
        public.lendBooks(book)
    else:
        value==False
