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


if __name__ == '__main__':
    add(lib)
    dell(lib)
    renew(lib)
