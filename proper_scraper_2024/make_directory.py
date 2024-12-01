import os
from pathlib import Path


def make_land_dir():
    home_path = Path.home()
    land_dir_name = "scrapiary"
    full_dir_name = home_path.joinpath(home_path, land_dir_name)

    if not full_dir_name.exists():
        os.chdir(home_path)
        os.mkdir(land_dir_name)
        #print(f"Done! Path is: {_path + land_dir_name} ")
    else:
        print(f"A directory named {land_dir_name} already exists! ")
        return full_dir_name

    return full_dir_name


# folder_name = dir_name.replace(':', '').replace('.','')