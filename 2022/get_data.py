import os
import sys

import requests
from dotenv import dotenv_values

# https://cloud.githubusercontent.com/assets/6615374/20862970/0922a4fe-b980-11e6-8f30-5967ca494f5e.png
default_year = 2022


def download(year, day):
    cookies = dict(session=dotenv_values()["session"])
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, cookies=cookies)
    if r.status_code == 200:
        return r.text
    else:
        return "Error with request", r.text


def save(year, day, data):
    file = f"inputs/day{day}.txt"
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write(data)


def load(year, day):
    file = f"inputs/day{day}.txt"
    with open(file) as f:
        text = [s.strip() for s in f.readlines()]
    return text


def get_data(year, day):
    file = f"inputs/day{day}.txt"
    if os.path.exists(file):
        data = load(year, day)
    else:
        data = download(year, day)
        save(year, day, data)
        data = load(year, day)
    return data


if __name__ == "__main__":
    if len(sys.argv) > 3:
        print("You have specified too many arguments")
        sys.exit()
    elif len(sys.argv) == 3:
        year = sys.argv[1]
        day = sys.argv[2]
        print(f"Getting data for {year}, day {day} \n")
    elif len(sys.argv) == 2:
        year = default_year
        day = sys.argv[1]
        print(f"Getting data for {year}, day {day} \n")

    data = get_data(year, day)

    print("First 10 lines of input file {file}:\n")
    print(os.linesep.join(data[:10]))
