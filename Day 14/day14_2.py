with open("input_14.txt", "r") as file:
    lines = file.readlines()

vel = []
pos = []
x_bound = 101
y_bound = 103
mid_y = y_bound//2
mid_x = x_bound//2
least_sf = float("inf")
tree_index = None
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

for s in range(1, x_bound*y_bound):    
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    for i in range(len(pos)):
        pos[i] = move(pos[i], vel[i])
        tup = pos[i]
        if 0 <= tup[0] < mid_x and 0 <= tup[1] < mid_y:
             q1 += 1
        elif mid_x < tup[0] < x_bound and 0 <= tup[1] < mid_y:
             q2+=1
        elif 0 <= tup[0] < mid_x and mid_y < tup[1] < y_bound:
             q3+=1
        elif mid_x < tup[0] < x_bound and mid_y < tup[1] < y_bound:
             q4+=1
    sf = q1*q2*q3*q4
    
    if sf < least_sf:
        least_sf = sf
        tree_index = s

print(tree_index, least_sf)
      


