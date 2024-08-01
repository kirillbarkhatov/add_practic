import os


def scan_dir(path_folder: str = os.getcwd(), recurs: bool = False) -> dict:
    """Принимает на вход путь до директории и возвращает словарь c количеством файлов и папок в ней"""

    if os.path.isdir(path_folder):
        count_files = 0
        count_folders = 0


        if recurs:
            for root, dirs, files in os.walk(path_folder):
                count_files += len(files)
                count_folders += len(dirs)



        else:
            dirs_files = os.scandir(path_folder)

            for obj in dirs_files:
                if obj.is_dir():
                    count_folders += 1
                else:
                    count_files += 1

        result = {
            "files": count_files,
            "folders": count_folders
        }
        return result

    return "Папки по указанному пути не существует или путь указан не верно"

if __name__ == "__main__":
    path = "/Users/kirill_barkhatov/PycharmProjects/add_practic/src"

    folder_info = scan_dir()
    print(folder_info)