import re


file = open("input_day3_2024.txt").read()

mul_pattern = r"mul\(\d+,\d+\)"
matches = re.findall(mul_pattern, file)
acc = 0
for i in range(len(matches)):
    multiplicators = re.findall(r"\d+", matches[i])
    acc += int(multiplicators[0]) * int(multiplicators[1])


print(matches)
print(acc)
