from get_data import get_data

# with open("../inputs/2022/day1ex.txt") as f:
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
