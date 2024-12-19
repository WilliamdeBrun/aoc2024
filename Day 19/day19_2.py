with open("input_19.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

colors = sorted(lines[0].split(", "), key=len, reverse=True)

towels = lines[2:]

calced = {}

def possible(towel):
    if not towel:
        return 1
    
    if towel in calced:
        return calced[towel]
    
    count = 0
    for color in colors:
        if towel.startswith(color):
            count += possible(towel[len(color):])

    calced[towel] = count           
    return count

total = 0

for towel in towels:
    total += possible(towel)
       

print(total)
