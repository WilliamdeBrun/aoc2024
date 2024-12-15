import copy
with open("input_15.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

nl_idx = lines.index('')

grid = [list(line) for line in lines[:nl_idx]]


moves = [token for line in lines[nl_idx+1:] for token in line]
rows = len(grid)
cols = len(grid[0])
robot = "@"
large_grid=[]
for row in range(rows):
    large_row = []
    for col in range(cols):
        token = grid[row][col]
        if token == "O":
            large_row.append("[")
            large_row.append("]")
        elif token == "@":
            large_row.append(token)
            large_row.append(".")
        else:
            large_row.append(token)
            large_row.append(token)
    large_grid.append(large_row)
large_cols = len(large_grid[0])
for row in range(rows):
    if robot in large_grid[row]:
        start_idx = (row, large_grid[row].index(robot))


def up(row, col, token, grid):
    moved = False
    if grid[row-1][col] == ".":
        grid[row-1][col] = token
        grid[row][col] = "."
        moved = True
    elif grid[row-1][col] == "[":
        new_grid = copy.deepcopy(grid)
        new_grid, moved1 = up(row-1, col, "[", new_grid)
        new_grid, moved2 = up(row-1, col+1, "]", new_grid)
        if moved1 and moved2:
            grid = new_grid
            grid[row-1][col] = token
            grid[row][col] = "."
            moved = True
    elif grid[row-1][col] == "]":
        new_grid = copy.deepcopy(grid)
        new_grid, moved1 = up(row-1, col, "]", new_grid)
        new_grid, moved2 = up(row-1, col-1, "[", new_grid)
        if moved1 and moved2:
            grid = new_grid
            grid[row-1][col] = token
            grid[row][col] = "."
            moved=True

    return grid, moved            
        

def down(row, col, token, grid):
    moved = False
    if grid[row+1][col] == ".":
        grid[row+1][col] = token
        grid[row][col] = "."
        moved = True
    elif grid[row+1][col] == "[":
        new_grid = copy.deepcopy(grid)
        new_grid, moved1 = down(row+1, col, "[", new_grid)
        new_grid, moved2 = down(row+1, col+1, "]", new_grid)
        if moved1 and moved2:
            grid = new_grid
            grid[row+1][col] = token
            grid[row][col] = "."
            moved=True
    elif grid[row+1][col] == "]":
        new_grid = copy.deepcopy(grid)
        new_grid, moved1 = down(row+1, col, "]", new_grid)
        new_grid, moved2 = down(row+1, col-1, "[", new_grid)
        if moved1 and moved2:
            grid = new_grid
            grid[row+1][col] = token
            grid[row][col] = "."
            moved=True

    return grid, moved 
def right(row, col, token, grid):
    moved = False
    if grid[row][col+1] == ".":
        grid[row][col+1] = token
        grid[row][col] = "."
        moved = True
    elif grid[row][col+1] == "[":
        grid, moved = right(row, col+1, "[", grid)
        if moved:
            grid[row][col+1] = token
            grid[row][col] = "."
    elif grid[row][col+1] == "]":
        grid, moved = right(row, col+1, "]", grid)
        if moved:
            grid[row][col+1] = token
            grid[row][col] = "["

    return grid, moved 
def left(row, col, token, grid):
    moved = False
    if grid[row][col-1] == ".":
        grid[row][col-1] = token
        grid[row][col] = "."
        moved = True
    elif grid[row][col-1] == "[":
        grid, moved = left(row, col-1, "[", grid)
        if moved:
            grid[row][col-1] = token
            grid[row][col] = "]"
    elif grid[row][col-1] == "]":
        grid, moved = left(row, col-1, "]", grid)
        if moved:
            grid[row][col-1] = token
            grid[row][col] = "."
    

    return grid, moved 


for move in moves:
    
    if move == "^":
        large_grid, moved = up(start_idx[0], start_idx[1], robot, large_grid)
        if moved:
            start_idx = (start_idx[0]-1, start_idx[1])
    elif move == ">":
        large_grid, moved = right(start_idx[0], start_idx[1], robot, large_grid)
        if moved:
            start_idx = (start_idx[0], start_idx[1]+1)
    elif move == "<":
        large_grid, moved = left(start_idx[0], start_idx[1], robot, large_grid)
        if moved:
            start_idx = (start_idx[0], start_idx[1]-1)
    else:
        large_grid, moved = down(start_idx[0], start_idx[1], robot, large_grid)
        if moved:
            start_idx = (start_idx[0]+1, start_idx[1])
    
    
total = 0

for row in range(rows):
    for col in range(large_cols):
        if large_grid[row][col] == "[":
            total += 100*row + col 


print(total)

