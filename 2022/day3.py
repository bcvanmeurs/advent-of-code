import string

from get_data import get_data

# with open("inputs/day3ex.txt") as f:
# data = [x.strip() for x in f]
data = get_data(2022, 3)


def find_duplicate(array: str):
    first = set(array[: len(array) // 2])
    second = set(array[len(array) // 2 :])
    return (first & second).pop()


alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
scores = {}
for letter, score in zip(alphabet, range(1, 53)):
    scores[letter] = score

print("Part 1:", sum(scores[find_duplicate(backpack)] for backpack in data))


def split(l):
    for i in range(0, len(l), 3):
        b1 = set(l[i])
        b2 = set(l[i + 1])
        b3 = set(l[i + 2])
        yield (b1 & b2 & b3).pop()


print("Part 2:", sum(scores[group] for group in split(data)))
