import re
from collections import deque

from get_data import get_data

get_data(2022, 5)

from collections import defaultdict

INDEXROW = 3
COLUMNS = 3
with open("inputs/2022/day5ex.txt") as f:
    lines = f.readlines()

INDEXROW = 8
COLUMNS = 9
with open("inputs/day5.txt") as f:
    lines = f.readlines()

xslice = slice(1, COLUMNS * 4, 4)

columns = defaultdict(deque)
columns_part2 = defaultdict(list)

for x in range(INDEXROW):
    [columns[i].appendleft(v) for i, v in enumerate(lines[x][xslice]) if v != " "]
    [columns_part2[i].insert(0, v) for i, v in enumerate(lines[x][xslice]) if v != " "]

# print("initial columns:", columns)

expr = re.compile(r"move (\d+) from (\d) to (\d)")

for i in range(INDEXROW + 2, len(lines)):
    m = expr.search(lines[i])
    number, source, dest = m.groups()
    source = int(source) - 1
    dest = int(dest) - 1
    for x in range(int(number)):
        columns[dest].append(columns[source].pop())
        columns_part2[dest].append(columns_part2[source].pop(-int(number) + x))

print("Part 1:", "".join([v.pop() for _, v in sorted(columns.items())]))
print("Part 2:", "".join([v.pop() for _, v in sorted(columns_part2.items())]))
