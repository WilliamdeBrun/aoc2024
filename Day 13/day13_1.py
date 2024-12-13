with open("input_13.txt", "r") as file:
    lines = file.readlines()

A = []
B = []
prize = []

for line in lines:
    if line.startswith("Button A"):
        x = int(line.split(":")[1].strip().split(", ")[0].split("+")[1])
        y = int(line.split(":")[1].strip().split(", ")[1].split("+")[1])
        A.append((x,y))
    elif line.startswith("Button B"):
        x = int(line.split(":")[1].strip().split(", ")[0].split("+")[1])
        y = int(line.split(":")[1].strip().split(", ")[1].split("+")[1])
        B.append((x,y))
    elif line.startswith("Prize"):
        x = int(line.split(":")[1].strip().split(", ")[0].split("=")[1])
        y = int(line.split(":")[1].strip().split(", ")[1].split("=")[1])
        prize.append((x,y))


def get_cheapest(a, b, p):
    cheapest = float("inf")
    for pa in range(100):
        for pb in range(100):
            x = pa * a[0] + pb * b[0]
            y = pa * a[1] + pb * b[1]
            if (x, y) == p:
                cost = pa * 3 + pb
                if cost < cheapest:
                    cheapest = cost
                    
    if cheapest == float("inf"):
        return 0
    return cheapest

total_cost = 0

for i in range(len(A)):
    total_cost += get_cheapest(A[i], B[i], prize[i])

print(total_cost)