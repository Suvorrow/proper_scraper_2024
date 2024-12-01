import wbgapi as wbi
import pandas as pd
import pathlib
from datetime import datetime as dtm
from make_directory import make_land_dir as land_dir_path


def create_dfr(db_pkg: str):
    db_pkg_ = db_pkg
    act_on_data = wbi.data.DataFrame(db_pkg_, time=range(2015, 2024), labels=True) \
        .round(decimals=1) \
        .sort_values('YR2023', ascending=False)

    return act_on_data


def write_dfr(ldpath: pathlib.PosixPath, filename: str, dataframe: pd.DataFrame):
    dfr_ = dataframe
    filename_ = ldpath.joinpath(filename)
    with open(filename_, 'w') as file:
        file.write(dfr_.to_string())

    return file


def indicators_list(indicat_in, ldpath_01, fl_nm):
    fl_nm_ = ldpath_01.joinpath(fl_nm)

    swap = {values: keys for keys, values in indicat_in.items()}

    swapped_indicats = pd.Series(swap)

    with open(fl_nm_, 'w') as onefile:
        onefile.write(swapped_indicats.to_string())

    return onefile


def auto_naming():
    #db_info = wbi.series.list()
    dt_tm = dtm.now().strftime("%Y%m%d_%H%M%S")

    return dt_tm


if __name__ == '__main__':
    l_dir = land_dir_path()
    naming = auto_naming()
    #create_dataframe = create_dfr('NY.GDP.PCAP.CD')
    specific_indicats = indicators_list(wbi.series.Series(), l_dir, naming)

    #make_file = write_file(l_dir, naming, create_dataframe)
