from library_1 import add, dell, renew, search


lib = {
            "title": "Белый дракон (роман)",
            "year": 2013,
            "pages": 547,
            "isbn13": 978-1-139-33287-3,
            "rating": 4,
            "price": 1500,
            "discount": 10,
            "author": 'Александр Стула'
        }


def display_menu():
    ...

def add_book(lib):
    input("Введите книгу:")
    add(lib=lib)


def dell_book(lib):
    input("Введите книгу:")
    dell(lib=lib)


def renew_book(lib):
    input("Введите книгу:")
    renew(lib=lib)


def search_book(lib):
    input("Введите книгу:")
    search(lib=lib)


def main():
    while True:
        display_menu()
        cmd = input()
        if cmd == '1':
            add_book(lib)
        elif cmd == '2':
            dell_book(lib)
        elif cmd == '3':
            renew_book(lib)
        elif cmd == '4':
            search_book(lib)


if __name__ == '__main__':
    main()