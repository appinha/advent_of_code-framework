import configparser
import shutil
import sys
import urllib.request
from configparser import MissingSectionHeaderError
from urllib.error import HTTPError

from utils import check_day, error, get_puzzle_url


def get_config():
    config = configparser.ConfigParser()
    try:
        config.read("../config.ini")
    except configparser.MissingSectionHeaderError:
        error("config.ini must contain a section header '[aoc_settings]'")
    try:
        settings = config["aoc_settings"]
        return settings["year"], settings["session_cookie"]
    except KeyError as err:
        error(f"no value found for {err} in config.ini")


def download_challenge(day: str, year: str, session_cookie: str):
    input_file_path = f"../day_{day}/input.txt"
    url = get_puzzle_url(day, year) + "/input"

    request = urllib.request.Request(url)
    request.add_header("Cookie", f"session={session_cookie}")

    try:
        with urllib.request.urlopen(request) as response, open(input_file_path, 'wb') as input_file:
            shutil.copyfileobj(response, input_file)
    except HTTPError as err:
        if err.code == 400:
            error("could not download input, please check if you have a valid session_cookie in config.ini")
        if err.code == 404:
            error("could not download input, please check if you have a valid year in config.ini")
        else:
            raise


if __name__ == '__main__':
    if len(sys.argv) < 2:
        error("no day was provided for downloading input")
    else:
        day = sys.argv[1]
        check_day(day)
        print(f"📥 Downloading input for day {day}...")
        year, session_cookie = get_config()
        download_challenge(day, year, session_cookie)
        print(f"✅ Successfully downloaded input!")
        print(f"🔗 Access the puzzle on {get_puzzle_url(day, year)}")
