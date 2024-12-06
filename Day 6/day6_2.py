import copy
with open("input_6.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]



dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rows = len(lines)
cols = len(lines[0])
guard = "^"
count = 0
guard_row = 0
guard_col = 0

def update_dir(curr_dir):
    dir_idx = dir.index(curr_dir)
    if dir_idx == len(dir)-1:
        dir_idx = 0
    else:
        dir_idx += 1
    return dir[dir_idx]

for row in range(rows):
    for col in range(cols):
        if lines[row][col] == guard:
            guard_row = row
            guard_col = col
            #lines[row][col] = "X"

def get_loops(curr_row, curr_col, temp_lines, curr_dir): 
    visited_obsts = []
    while(0 < curr_row < rows-1 and 0 < curr_col < cols-1):
        next_row = curr_row+curr_dir[0]
        next_col = curr_col+curr_dir[1]
        if temp_lines[next_row][next_col] == "#":
            if (next_row, next_col, curr_dir) in visited_obsts:
                return True
            visited_obsts.append((next_row, next_col, curr_dir))
            curr_dir=update_dir(curr_dir)
        else:
            curr_row = next_row
            curr_col = next_col
            
            #if lines[curr_row][curr_col] == ".":
             #   lines[curr_row][curr_col] = "X"
                #count += 1
    return False

for row in range(rows):
    for col in range(cols):
        if lines[row][col] != guard:
            curr_dir = dir[0]
            temp_lines = copy.deepcopy(lines)
            temp_lines[row][col] = "#"
            if get_loops(guard_row, guard_col, temp_lines, curr_dir):
                count += 1
            #lines[row][col] = "X"


print(count)
