from collections import Counter

from get_data import get_data

# with open("inputs/day2ex.txt") as f:
# data = [x.strip() for x in f]

data = get_data(2022, 2)

"""
A X rock
B Y paper
C Z scissor
"""

scoresa = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}

counts = Counter(data)
print(f"Part a: {sum(scoresa[k] * v for k, v in counts.items())}")

scoresb = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}
print(f"Part b: {sum(scoresb[k] * v for k, v in counts.items())}")
