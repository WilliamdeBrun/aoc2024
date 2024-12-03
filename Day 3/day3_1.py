import re
from math import prod

with open("day3_input.txt", "r") as file:
    input = file.read()


valid_ops = [(int(x), int(y)) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)]
mults = 0
for op in valid_ops:
    mults += prod(op)

print(mults)