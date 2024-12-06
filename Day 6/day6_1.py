with open("input_6.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]



dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]
rows = len(lines)
cols = len(lines[0])
guard = "^"
count = 1
curr_dir = dir[0]
curr_row = 0
curr_col = 0

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
            curr_row = row
            curr_col = col
            lines[row][col] = "X"


while(0 < curr_row < rows-1 and 0 < curr_col < cols-1):
    if lines[curr_row+curr_dir[0]][curr_col+curr_dir[1]] == "#":
        curr_dir=update_dir(curr_dir)
    else:
        curr_row += curr_dir[0]
        curr_col += curr_dir[1]
        if lines[curr_row][curr_col] == ".":
            lines[curr_row][curr_col] = "X"
            count += 1
            
print(count)
