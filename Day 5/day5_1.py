import re
with open("input_5.txt", "r") as file:
    input = file.read()

rules = [(int(x), int(y)) for x, y in re.findall(r"(\d+)\|(\d+)", input)]

lines = input.splitlines()
blank_idx = lines.index('')
all_pages = []    
    
for i in range(blank_idx+1, len(lines)):
    all_pages.append([int(x) for x in lines[i].split(',')])

middle_sum = 0

for pages in all_pages:
    valid_page = True
    for j in range(len(pages)-1):
        for rule in rules:
            if rule == (pages[j+1], pages[j]):
                valid_page = False
    if valid_page:
        middle_sum += pages[(len(pages))//2]

print(middle_sum)