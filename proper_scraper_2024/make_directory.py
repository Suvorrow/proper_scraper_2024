import os


def make_land_dir():
    _path = os.path.expanduser("~")
    land_dir_name = ".Scrapiary"

    if not os.path.exists(_path + land_dir_name):
        os.chdir(_path)
        os.mkdir(land_dir_name)
    else:
        print(f"A directory named {land_dir_name} already exists! ")
    return


my_def = make_land_dir()



# folder_name = dir_name.replace(':', '').replace('.','')