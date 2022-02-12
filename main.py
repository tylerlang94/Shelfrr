import library
import menu as m


def main():
    books = library.books_dict()
    m.library_menu()

    while True:
        option = input('Option: ')
        print('')
        if option == 'add':
            m.add_book(books)
        elif option == 'delete':
            m.del_book(books)
        elif option == 'show':
            m.show_book(books)
        elif option == 'title':
            m.search_title(books)
        elif option == 'author':
            m.search_author(books)
        elif option == 'quit':
            break
        else:
            print('Invalid Option: Please input an option from the list')


main()
