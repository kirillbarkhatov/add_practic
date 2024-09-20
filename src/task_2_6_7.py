def file_close(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper

#
# @file_close
# def file_open(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         print(file.read())
#     print(file.closed)


@file_close
def file_open_open(file_path):
    file = open(file_path, "r", encoding="utf-8")
    print(file.read())
    file.close()


# file_open("/Users/kirill_barkhatov/PycharmProjects/add_practic/src/example.txt")
file_open_open("/Users/kirill_barkhatov/PycharmProjects/add_practic/src/example.txt")

