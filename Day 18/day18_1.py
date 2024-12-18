from collections import deque
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

for i in range(b):
    row = coords[i][0]
    col = coords[i][1]
    grid[row][col] = "#"


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

print(find_path(grid))