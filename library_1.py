import json
FILENAME = 'lib_json'



def to_json(obj):
    with open(obj, 'r') as file:
        lib = json.load(file)
    return lib


def to_json_lib(obj):
    with open(FILENAME, 'w') as file:
        json.dump(obj, file, indent=4)


if __name__ == '__main__':
    to_json(lib)



