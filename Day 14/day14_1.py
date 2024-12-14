with open("input_14.txt", "r") as file:
    lines = file.readlines()

vel = []
pos = []
x_bound = 101
y_bound = 103
mid_y = y_bound//2
mid_x = x_bound//2
for line in lines:
        px = int(line.split(" ")[0].split("=")[1].split(",")[0])
        py = int(line.split(" ")[0].split("=")[1].split(",")[1])
        vx = int(line.split(" ")[1].split("=")[1].split(",")[0])
        vy = int(line.split(" ")[1].split("=")[1].split(",")[1])
        vel.append((vx, vy))
        pos.append((px, py))


def move(p, v):
    
    if  0 <= p[0] + v[0] < x_bound:
        x = p[0] + v[0]
    elif p[0] + v[0] >= x_bound:
        x = p[0] + v[0] - x_bound
    else:
         x = x_bound + (p[0] + v[0])


    if  0 <= p[1] + v[1] < y_bound:
        y = p[1] + v[1]
    elif p[1] + v[1] >= y_bound:
        y = p[1] + v[1] - y_bound
    else:
         y = y_bound + (p[1] + v[1])
    return (x, y)

for _ in range(100):    
    for i in range(len(pos)):
        pos[i] = move(pos[i], vel[i])

quad_1 = [tup for tup in pos if 0 <= tup[0] < mid_x and 0 <= tup[1] < mid_y]
quad_2 = [tup for tup in pos if mid_x < tup[0] < x_bound and 0 <= tup[1] < mid_y]
quad_3 = [tup for tup in pos if 0 <= tup[0] < mid_x and mid_y < tup[1] < y_bound]
quad_4 = [tup for tup in pos if mid_x < tup[0] < x_bound and mid_y < tup[1] < y_bound]

print(len(quad_1)*len(quad_2)*len(quad_3)*len(quad_4))       


