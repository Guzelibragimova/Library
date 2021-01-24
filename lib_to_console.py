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
    """
    Функция добавляет новое название книги
    :param lib:
    :return:
    """
    a = input("Введите книгу для добавления: ")
    lib['title'] = a
    print(lib)


def dell(lib):
    """
    Функция по ключу удаляет пару: ключ : значение
    :param lib:
    :return:
    """
    a = input("Введите ключ для удаления из словаря: ")
    if a == "author":
        del lib["author"]
        print(lib)
    if a == "title":
        del lib["title"]
        print(lib)
    if a == "year":
        del lib["year"]
        print(lib)
    if a == "pages":
        del lib["pages"]
        print(lib)
    if a == "isbn13":
        del lib["isbn13"]
        print(lib)
    if a == "rating":
        del lib["rating"]
        print(lib)
    if a == "price":
        del lib["price"]
        print(lib)
    if a == "discount":
        del lib["discount"]
        print(lib)


def renew(lib):
    """
    Функция перезаписывает название книги
    :param lib:
    :return:
    """
    a = input("Введите новое название книги: ")
    lib['title'] = a
    print(lib)


def search(lib):
    """
    Функция ищет автора и выводит его имя фамилию
    :param lib:
    :return:
    """
    a = input('Введите название автора для поиска: ')
    if a == lib["author"]:
        author_in_lib = lib.get("author")
        print(author_in_lib)
    if a != lib["author"]:
        print("Данного автора нет в библиотеке")


def display_menu():
    print("There is a library")


def add_book(lib):
    add(lib)


def dell_book(lib):
    dell(lib=lib)


def renew_book(lib):
    renew(lib=lib)


def search_book(lib):
    search(lib=lib)


def main():
    while True:
        display_menu()
        cmd = input("Введите число от 1 до 4: ")
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
