from itertools import product

from get_data import get_data

get_data(2022, 8)

with open("inputs/day8.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]


height = len(lines)
width = len(lines[0])
visible = [[False] * height for _ in range(width)]

for x, y in product(range(width), range(height)):
    # trees at the boundaries are visible
    if x == 0 or y == 0:
        visible[y][x] = True
    else:
        h = lines[y][x]
        row = lines[y]
        column = [lines[j][x] for j in range(height)]
        if (
            h > max(row[0:x], default=-1)
            or h > max(row[x + 1 :], default=-1)
            or h > max(column[0:y], default=-1)
            or h > max(column[y + 1 :], default=-1)
        ):
            visible[y][x] = True

print("Part 1:", sum(sum(x) for x in visible))
