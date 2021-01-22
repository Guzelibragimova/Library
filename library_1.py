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


def search(lib):
    """
    Функция ищет автора и выводит его имя фамилию

    :param lib:
    :return:
    """

    print(lib.get("author"))





if __name__ == '__main__':
    search(lib)