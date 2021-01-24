import json
FILENAME = 'lib_json'

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


def to_json():
    """
    Сохраняем в json

    :return:
    """
    with open('lib.json', 'w', encoding='utf-8') as file:  # открываем файл на запись
        file.write(json.dumps(lib, ensure_ascii=False, indent=4))


def to_json_lib():
    """
    Загружаем из json

    :return: словарь lib
    """
    with open('lib.json', 'r', encoding='utf-8') as file:  # открываем файл на чтение
        lib1 = json.load(file)  # загружаем из файла данные в словарь lib
    return lib1


if __name__ == '__main__':
    to_json()
    to_json_lib()
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
