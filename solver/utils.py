def check_day(day: str):
    try:
        day = int(day)
    except ValueError:
        error("please provide a valid number for day")
    if not (1 <= day <= 25):
        error("day must be a number between 1 and 25")


def check_part(part: str):
    try:
        part = int(part)
    except ValueError:
        error("please provide a valid number for part")
    if not (1 <= part <= 2):
        error("part must be a number between 1 and 2")


def error(msg: str):
    print(f"❌ Error: {msg}")
    exit()


def get_puzzle_url(day: str, year: str):
    return f"https://adventofcode.com/{year}/day/{str(int(day))}"
