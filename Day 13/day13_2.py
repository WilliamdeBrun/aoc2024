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
        x = int(line.split(":")[1].strip().split(", ")[0].split("=")[1]) + 10000000000000
        y = int(line.split(":")[1].strip().split(", ")[1].split("=")[1]) + 10000000000000
        prize.append((x,y))


def get_cheapest(a, b, p):
    ap, bp = (p[0]*b[1]-p[1]*b[0])//(b[1]*a[0]-b[0]*a[1]), (p[0]*a[1]-p[1]*a[0])//(a[1]*b[0]-b[1]*a[0])
    if (a[0]*ap + b[0]*bp, a[1]*ap + b[1]*bp) == p:
        return 3*ap+bp
    return 0

    

total_cost = 0

for i in range(len(A)):
    total_cost += get_cheapest(A[i], B[i], prize[i])

print(total_cost)