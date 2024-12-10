with open("input_10.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]
    
rows = len(lines)
cols = len(lines[0])
trails = 0
directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

def count_trails(row, col, visited):
    if (row, col) in visited:
        return 0
    
    visited.append((row, col))
    cur_node = int(lines[row][col])

    if cur_node == 9:
        return 1
    
    cur_trails = 0
    for dir in directions:
        new_row = row + dir[0]
        new_col = col + dir[1]
        if not (0<=new_row<rows and 0 <=new_col<cols):
            continue
        next_node = int(lines[new_row][new_col])
        if next_node == cur_node + 1:
            cur_trails += count_trails(new_row, new_col, visited)
    return cur_trails
        


for row in range(rows):
    for col in range(cols):
        if lines[row][col] == '0':
            trails += count_trails(row, col, [])

print(trails)