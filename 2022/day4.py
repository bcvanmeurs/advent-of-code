from get_data import get_data

with open("inputs/day4ex.txt", "r") as f:
    data = [x.strip() for x in f]
data = get_data(2022, 4)

data = list(row.split(",") for row in data)


def has_overlap(row):
    l1, r1 = row[0].split("-")
    l2, r2 = row[1].split("-")

    return (int(l1) >= int(l2) and int(r1) <= int(r2)) or (
        int(l2) >= int(l1) and int(r2) <= int(r1)
    )


print("Part 1:", sum(has_overlap(row) for row in data))


def has_partial_overlap(row):
    l1, r1 = row[0].split("-")
    l2, r2 = row[1].split("-")

    return int(l2) <= int(l1) <= int(r2) or int(l1) <= int(l2) <= int(r1)


print("Part 2:", sum(has_partial_overlap(row) for row in data))
