with open("input_19.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

colors = sorted(lines[0].split(", "), key=len, reverse=True)

towels = lines[2:]


def possible(towel):
    if not towel:
        return True
    for color in colors:
        if towel.startswith(color):
            if possible(towel[len(color):]):
                return True
    return False

total = 0

for towel in towels:
    if possible(towel):
        total += 1

print(total)
