filelines = open("input_day2_2024.txt").read().splitlines()
reps = []
for i in range(len(filelines)):
    l_tmp = filelines[i].split()
    l_tmp2 = [int(x) for x in l_tmp]
    reps.append(l_tmp2)


def part1(reports):
    safe = 0
    for i in range(len(reports)):
        if is_safe(reports[i]):
            safe += 1
    print(safe)


def part2(reports):
    safe = 0
    for i in range(len(reports)):
        if is_safe(reports[i]):
            safe += 1
            continue
        for j in range(len(reports[i])):
            repop = reports[i][:]
            repop.pop(j)
            if is_safe(repop):
                safe += 1
                break
    print(safe)


def is_safe(report):
    increasing = True
    for i in range(len(report) - 1):
        curr = report[i]
        next = report[i + 1]
        if abs(curr - next) < 1 or abs(curr - next) > 3:
            return False
        if i == 0:
            if curr < next:
                increasing = True
            else:
                increasing = False
        if increasing:
            if curr > next:
                return False
        else:
            if curr < next:
                return False
    return True


# part1(reps)
part2(reps)
