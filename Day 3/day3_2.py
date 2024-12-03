import re
from math import prod
import numpy as np
with open("day3_input.txt", "r") as file:
    input = file.read()

valid_ops = [(int(x), int(y)) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", input)]
mult_ind = [x.start() for x in re.finditer(r"mul\((\d{1,3}),(\d{1,3})\)", input)]
dos = [x.start() for x in re.finditer(r"(do\(\))", input)]
donts = [x.start() for x in re.finditer(r"(don't\(\))", input)]

mults = 0
dos.insert(0, 0)

for i in range(len(mult_ind)):
    valid = True
    closest = 0
    dist = np.inf
    
    for do in dos:
        if 0 <= (mult_ind[i] - do) < dist:
            closest = do
            dist = mult_ind[i]-do
            

    for dont in donts:
        if 0 <= (mult_ind[i] - dont) < dist:
            closest = dont
            dist = mult_ind[i]-dont
            valid = False
    if valid:
        mults += prod(valid_ops[i])

print(mults)