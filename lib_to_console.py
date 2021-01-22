from library_1 import add, dell, renew




def display_menu():

def add_book():
    input("Введите книгу")
    add(lib=lib)

def main():
    while True:
        display_menu()
        cmd = input()
        if cmd == '1':
            add_book()

if __name__ == '__main__':
    main()