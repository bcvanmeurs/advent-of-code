from get_data import get_data

get_data(2022, 8)

with open("inputs/day8.txt") as f:
    lines = [[int(y) for y in x.strip()] for x in f.readlines()]


def is_visible(line, visible) -> list[bool]:
    _max = -1

    for i, height in enumerate(line):
        if height > _max:
            visible[i] = True
        _max = max(_max, height)

    _max = -1
    for i, height in enumerate(reversed(line)):
        if height > _max:
            visible[~i] = True
        _max = max(_max, height)

    return visible


def transpose(lines):
    return [list(x) for x in zip(*lines)]


visibles = []

for line in lines:
    visible = [False] * len(line)
    visible = is_visible(line, visible)
    visibles.append(visible)


lines = transpose(lines)
visibles = transpose(visibles)

visibles_2 = []

for line, visible in zip(lines, visibles):
    visible = is_visible(line, visible)
    visibles_2.append(visible)

print("Part 1:", sum(sum(x) for x in visibles_2))
