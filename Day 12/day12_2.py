with open("input_12.txt", "r") as file:
    lines =  [x.strip() for x in file.readlines()]

rows = len(lines)
cols = len(lines[0])
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()
cost = 0

        
def get_regions(row, col, visited, target, cur_visited):
    if (row, col) in visited:
        return 0, cur_visited
    cur_visited.append((row, col))
    visited.add((row, col))
    area = 1
    for dir in dirs:
        new_row = row+dir[0]
        new_col = col+dir[1]
        if 0 <= new_row < rows and 0 <= new_col < cols and lines[new_row][new_col] == target:
            new_area, cur_visited = get_regions(new_row, new_col, visited, target, cur_visited) 
            area += new_area
    
    return area, cur_visited

def get_sides(visited):
    up, down, left, right = set(), set(), set(), set()
    for (row, col) in visited:
        if (row-1, col) not in visited:
            up.add((row-1, col))
        if (row+1, col) not in visited:
            down.add((row-1, col))
        if (row, col-1) not in visited:
            left.add((row-1, col))
        if (row, col+1) not in visited:
            right.add((row-1, col))
    sides = 0
    for (row, col) in up:
        if (row, col) in left:
            sides+=1
        if (row,col) in right:
            sides+=1
        if (row-1, col-1) in right and (row, col) not in left:
            sides+=1
        if (row-1, col+1) in left and (row, col) not in right:
            sides+=1
    for (row, col) in down:
        if (row, col) in left:
            sides+=1
        if (row,col) in right:
            sides+=1
        if (row+1, col-1) in right and (row, col) not in left:
            sides+=1
        if (row+1, col+1) in left and (row, col) not in right:
            sides+=1
    return sides

for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            target = lines[row][col]
            cur_area, cur_visited = get_regions(row, col, visited, target, [])
            cost += cur_area*get_sides(cur_visited)

print(cost)


