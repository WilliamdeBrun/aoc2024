from collections import deque
from copy import deepcopy
with open("input_18.txt", "r") as file:
    coords = [tuple(map(int, line.strip().split(','))) for line in file]

grid_size = 70
b = 1024
start = 0
grid = []
for _ in range(grid_size+1):
    row = []
    for _ in range(grid_size+1):
        row.append(".")
    grid.append(row)
def add_blocks(grid_blocks, bs):
    for i in range(bs):
        row = coords[i][0]
        col = coords[i][1]
        grid_blocks[row][col] = "#"
    return grid_blocks


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def find_path(grid):
    queue = deque([(0, start, start)])
    visited = set()
    visited.add((start, start))
    
    while queue:
        cost, row, col = queue.popleft()
        if row == grid_size and col == grid_size:
            return cost
        
        for dir_r, dir_c in dirs:
            new_row, new_col = row+dir_r, col+dir_c
            if 0 <= new_row <= grid_size and 0 <= new_col <= grid_size and grid[new_row][new_col] != '#' and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                queue.append((cost+1, new_row, new_col))
                
    
    return float('inf')

left = 0
right = len(coords)-1
first_idx = -1
while left <= right:
    half = left + (right - left)//2
    grid_copy = deepcopy(grid)
    grid_copy = add_blocks(grid_copy, half+1)
    if find_path(grid_copy) == float('inf'):
        first_idx = half
        right = half - 1
    else:
        left = half + 1

print(coords[first_idx])
   

