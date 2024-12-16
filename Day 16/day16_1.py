import heapq
with open("input_16.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
rows = len(grid)
cols = len(grid[0])
for row in range(rows):
    for col in range(cols):
        if grid[row][col] == "S":
            start_col = col
            start_row = row
        elif grid[row][col] == "E":
            end_col = col
            end_row = row


def find_path(grid):
    queue = []
    heapq.heappush(queue, (0, start_row, start_col, (0, 1)))
    visited = {(start_row, start_col, (0,1))}
    
    while queue:
        cost, row, col, prev_dir = heapq.heappop(queue)
        visited.add((row, col, prev_dir))
        if row == end_row and col == end_col:
            return cost
        
        for dir_r, dir_c in dirs:
            new_row, new_col = row+dir_r, col+dir_c
            if grid[new_row][new_col] != '#':
                
                if sum(r * c for r, c in zip(prev_dir, (dir_r, dir_c))) == 0:
                    new_cost = cost + 1001
                else:
                    new_cost = cost + 1
                cur = (new_row, new_col, (dir_r, dir_c))
                if cur not in visited:
                    heapq.heappush(queue, (new_cost, new_row, new_col, (dir_r, dir_c)))
    
    return float('inf')

print(find_path(grid))
