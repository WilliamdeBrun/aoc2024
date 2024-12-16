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
    heapq.heappush(queue, (0, start_row, start_col, (0, 1), [(start_row, start_col)]))
    visited = {(start_row, start_col, (0,1))}
    cheapest = float('inf')
    best_paths = []

    while queue:
        
        cost, row, col, prev_dir, path = heapq.heappop(queue)
        visited.add((row, col, prev_dir))
        if cost > cheapest:
            continue
        if row == end_row and col == end_col:
            if cost < cheapest:
                cheapest = cost
                best_paths = [path]
            elif cost == cheapest:
                best_paths.append(path)
            
        for dir_r, dir_c in dirs:
            new_row, new_col = row+dir_r, col+dir_c
            if grid[new_row][new_col] != '#':
                
                if sum(r * c for r, c in zip(prev_dir, (dir_r, dir_c))) == 0:
                    new_cost = cost + 1001
                else:
                    new_cost = cost + 1
                cur = (new_row, new_col, (dir_r, dir_c))
                if cur not in visited:
                    heapq.heappush(queue, (new_cost, new_row, new_col, (dir_r, dir_c), path + [(new_row, new_col)]))
    return cheapest, best_paths

cheapest, best_paths = find_path(grid)
unique = set()
for path in best_paths:
    unique.update(path)
print(len(unique))
print(cheapest)