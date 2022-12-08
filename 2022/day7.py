from __future__ import annotations

from get_data import get_data

get_data(2022, 7)

with open("inputs/day7.txt") as f:
    lines = [x.strip() for x in f.readlines()]


class directory:
    name: str
    files: dict
    children: dict[str, directory]
    parent: directory
    _size: int

    def __init__(self, name, parent) -> None:
        self.name = name
        self.files = {}
        self._size = 0
        self.children = {}
        self.parent = parent

    def add_file(self, name, size) -> None:
        self.files[name] = size
        self._size += size

    def add_children(self, child: directory) -> None:
        self.children[child.name] = child

    def get_parent(self) -> directory:
        return self.parent

    def __repr__(self) -> str:
        return f"name: {self.name}, files {self._size}, children {self.children}"

    @property
    def size(self) -> int:
        return self._size + sum(c.size for c in self.children.values())


root = directory("/", None)
current = root

for line in lines[1:]:
    splitline = line.split(" ")
    if splitline[1] == "ls":
        ...
    elif splitline[1] == "cd":
        if splitline[2] == "..":
            current = current.get_parent()
        else:
            current = current.children[splitline[2]]
    elif splitline[0] == "dir":
        current.add_children(directory(splitline[1], current))
    else:
        current.add_file(splitline[1], int(splitline[0]))

stack = [root]
Sum = 0
part2 = []

while stack:
    current = stack.pop()
    stack.extend((c for c in current.children.values()))
    if current.size < 100000:
        Sum += current.size
    if current.size > root.size - 40000000:  # 30000000 - (70000000 - root.size)
        part2.append(current.size)

print("Part 1:", Sum)
print("Part 2:", sorted(part2)[0])
