
def library_menu():
    print('COMMAND    DESCRIPTION \n')
    print('all    |   show all books\n')
    print('add    |   add a book')
    print('delete |   delete a book\n')
    print('title  |   search by title')
    print('author |   search by author\n')
    print('quit   |   quit the program \n')
    print('******************************\n')


def add_book(books):
    book_title = input('What is the title of the book? ')
    book_author = input('What is the author of the book? ')
    books[book_title] = book_author
    return books


def show_book(books):
    count = str(len(books))
    print("There are " + count + " books in your library! \n")
    for book in books.keys():
        print(book + " by " + str(books[book]))
        print(' ')
    return books


def del_book(books):
    book_delete = input('What book do you want to delete? ')
    books.pop(book_delete, None)
    return books


def search_title(books):
    title = input("What title are you wanting to search for? ")
    print('')
    for key, value in books.items():
        if key == title.lower():
            print("That title is in the library!")
            break
        if key != title.lower():
            print("That title is not in the library. Please add it!")
            break


def search_author(books):
    author = input("What is the author you wanting to search for? ")
    print('')
    for key, value in books.items():
        if value == author.lower():
            print("That author is in the library!")
            break
        if value != author.lower():
            print("That author is not in the library.")
            break

