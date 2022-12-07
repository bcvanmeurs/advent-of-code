from get_data import get_data

# with open("inputs/day1ex.txt") as f:
# data = [x.strip() for x in f]
data = get_data(2022, 1)


elfs = []
Sum = 0
for x in data:
    if x == "":
        elfs.append(Sum)
        Sum = 0
    else:
        Sum += int(x)

print("Part 1:", max(elfs))
print("Part 2:", sum(sorted(elfs)[-3:]))

# Alternative solution without stripping and splitting on \n
with open("inputs/day1.txt") as f:
    data = f.read()

elves = sorted(sum(map(int, x.split("\n"))) for x in data[:-1].split("\n\n"))

print(f"Part 1: {elves[-1]}")
print(f"Part 2: {sum(elves[-3:])}")
