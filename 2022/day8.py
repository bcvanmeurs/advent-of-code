from itertools import product

from get_data import get_data

get_data(2022, 8)

with open("inputs/day8.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]


height = len(lines)
width = len(lines[0])
visible = [[False] * height for _ in range(width)]


def distance(h, vector):
    return next((i for i, tree in enumerate(vector) if tree >= h), len(vector) - 1) + 1


max_score = 0

for x, y in product(range(width), range(height)):
    # trees at the boundaries are visible
    h = lines[y][x]
    row = lines[y]
    column = [lines[j][x] for j in range(height)]
    if x == 0 or y == 0:
        visible[y][x] = True
    else:
        if (
            h > max(row[0:x], default=-1)
            or h > max(row[x + 1 :], default=-1)
            or h > max(column[0:y], default=-1)
            or h > max(column[y + 1 :], default=-1)
        ):
            visible[y][x] = True

    # Part 2
    left = distance(h, row[0:x][::-1])
    right = distance(h, row[x + 1 :])
    up = distance(h, column[0:y][::-1])
    down = distance(h, column[y + 1 :])
    score = left * right * up * down

    max_score = max(max_score, score)

print("Part 1:", sum(sum(x) for x in visible))
print("Part 2:", max_score)
