with open("input_15.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

nl_idx = lines.index('')

grid = [list(line) for line in lines[:nl_idx]]




moves = [token for line in lines[nl_idx+1:] for token in line]
rows = len(grid)
cols = len(grid[0])
robot = "@"
for row in range(rows):
    if robot in grid[row]:
        start_idx = (row, grid[row].index(robot))


def up(row, col, token, grid):
    moved = False
    if grid[row-1][col] == ".":
        grid[row-1][col] = token
        grid[row][col] = "."
        moved = True
    elif grid[row-1][col] == "O":
        grid, moved = up(row-1, col, "O", grid)
        if moved:
            grid[row-1][col] = token
            grid[row][col] = "."

    return grid, moved            
        

def down(row, col, token, grid):
    moved = False
    if grid[row+1][col] == ".":
        grid[row+1][col] = token
        grid[row][col] = "."
        moved = True
    elif grid[row+1][col] == "O":
        grid, moved = down(row+1, col, "O", grid)
        if moved:
            grid[row+1][col] = token
            grid[row][col] = "."

    return grid, moved 
def right(row, col, token, grid):
    moved = False
    if grid[row][col+1] == ".":
        grid[row][col+1] = token
        grid[row][col] = "."
        moved = True
    elif grid[row][col+1] == "O":
        grid, moved = right(row, col+1, "O", grid)
        if moved:
            grid[row][col+1] = token
            grid[row][col] = "."

    return grid, moved 
def left(row, col, token, grid):
    moved = False
    if grid[row][col-1] == ".":
        grid[row][col-1] = token
        grid[row][col] = "."
        moved = True
    elif grid[row][col-1] == "O":
        grid, moved = left(row, col-1, "O", grid)
        if moved:
            grid[row][col-1] = token
            grid[row][col] = "."

    return grid, moved 


for move in moves:
    if move == "^":
        grid, moved = up(start_idx[0], start_idx[1], robot, grid)
        if moved:
            start_idx = (start_idx[0]-1, start_idx[1])
    elif move == ">":
        grid, moved = right(start_idx[0], start_idx[1], robot, grid)
        if moved:
            start_idx = (start_idx[0], start_idx[1]+1)
    elif move == "<":
        grid, moved = left(start_idx[0], start_idx[1], robot, grid)
        if moved:
            start_idx = (start_idx[0], start_idx[1]-1)
    else:
        grid, moved = down(start_idx[0], start_idx[1], robot, grid)
        if moved:
            start_idx = (start_idx[0]+1, start_idx[1])

    
total = 0
count = 0
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "O":
            count += 1
            total += 100*row + col

    

print(total)

