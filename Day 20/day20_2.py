import heapq
with open("input_20.txt", "r") as file:
    grid = [list(line.strip()) for line in file.readlines()]

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
cheats = [(-1, -1), (-1, 1), (1, 1), (1, -1), (2, 0), (-2, 0), (0, 2), (0, -2)]
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
    heapq.heappush(queue, (0, start_row, start_col))
    visited = {(start_row, start_col)}
    path = {}
    
    while queue:
        cost, row, col = heapq.heappop(queue)
        visited.add((row, col))
        path[(row, col)] = cost

        if row == end_row and col == end_col:
            return cost, path
        
        for dir_r, dir_c in dirs:
            new_row, new_col = row+dir_r, col+dir_c
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] != '#':
                new_cost = cost + 1
                cur = (new_row, new_col)
                if cur not in visited:
                    heapq.heappush(queue, (new_cost, new_row, new_col))
    
    return float('inf'), path

no_cheat, visited_path = find_path(grid)
scores = []
for row in range(rows):
    for col in range(cols):
        if (row, col) in visited_path:
            for cheat_steps in range(2, 21):
                for cheat_r in range(cheat_steps+1):
                    cheat_c = cheat_steps-cheat_r
                    new_coords = set([(row+cheat_r, col+cheat_c), (row-cheat_r, col-cheat_c), (row-cheat_r, col+cheat_c), (row+cheat_r, col-cheat_c)])
                    for new_row, new_col in new_coords:
                        if (new_row, new_col) in visited_path:
                            score = visited_path[(new_row, new_col)] - visited_path[(row, col)] - cheat_steps
                            if score >= 100:
                                scores.append(score)



print(len(scores))
