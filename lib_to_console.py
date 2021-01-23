# from library_1 import add, dell, renew, search

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


def add(lib):
    lib['book'] = "Отцы и дети"
    print(lib)


def dell(lib):
    del lib['title']
    print(lib)


def renew(lib):
    lib["author"] = "Иван Тургенев"
    print(lib)


def search(lib):
    """
    Функция ищет автора и выводит его имя фамилию

    :param lib:
    :return:
    """
    print(lib.get("author"))


def display_menu():
    ...

def add_book(lib):
    input("Введите книгу для добавления:")
    add(lib=lib)


def dell_book(lib):
    input("Введите книгу для удаления:")
    dell(lib=lib)


def renew_book(lib):
    input("Введите книгу для обновления информации:")
    renew(lib=lib)


def search_book(lib):
    input("Введите книгу для поиска:")
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