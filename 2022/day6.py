from get_data import get_data

get_data(2022, 6)

with open("../inputs/2022/day6.txt") as f:
    lines = f.readlines()

# signal = "bvwbjplbgvbhsrlpgdmjqwftvncz"
signal = lines[0]

for i in range(len(signal) - 3):
    # print(signal[i : i + 4])
    if len(set(signal[i : i + 4])) == 4:
        res = i
        # print(res)
        break

print(res + 4)

for i in range(len(signal) - 13):
    # print(signal[i : i + 4])
    if len(set(signal[i : i + 14])) == 14:
        res = i
        # print(res)
        break

print(res + 14)
