import os
import shutil
import sys

from utils import build_directory_name, check_day, error, normalize_day


if __name__ == '__main__':
    if len(sys.argv) < 1:
        error("no day was provided for downloading input")
    else:
        day = sys.argv[1]
        check_day(day)
        directory = build_directory_name(day)
        if os.path.isdir(directory):
            error("folder already exists")
        else:
            try:
                shutil.copytree("day_template", directory)
                print(f"✅ Successfully created day_{normalize_day(day)} folder!")
                os.system(f"python solver/get_input.py {day}")
            except OSError:
                raise
