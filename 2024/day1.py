import numpy as np

file = open("input_day1_2024.txt")
unparsedl = file.read().split()

l1 = []
l2 = []
for i in range(len(unparsedl)):
    if i % 2 == 0:
        l1.append(unparsedl[i])
    else:
        l2.append(unparsedl[i])


def part1():
    distance = 0
    l1sort = sorted(l1)
    l2sort = sorted(l2)

    for i in range(len(l1sort)):
        distance += abs(int(l1sort[i]) - int(l2sort[i]))

    print(distance)


def part2():
    d = {}
    for i in range(len(l2)):
        try:
            d[l2[i]] += 1
        except KeyError:
            d[l2[i]] = 1
    sum = 0
    for i in range(len(l1)):
        try:
            sum += int(l1[i]) * d[l1[i]]
        except KeyError:
            continue
    print(sum)


part1()
part2()
