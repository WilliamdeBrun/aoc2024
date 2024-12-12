with open("input_12.txt", "r") as file:
    lines =  [x.strip() for x in file.readlines()]

rows = len(lines)
cols = len(lines[0])
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
visited = set()
cost = 0

        
def get_regions(row, col, visited, target):
    if (row, col) in visited:
        return 0, 0
    
    visited.add((row, col))
    area = 1
    neigbors = 4

    for dir in dirs:
        new_row = row+dir[0]
        new_col = col+dir[1]
        if 0 <= new_row < rows and 0 <= new_col < cols and lines[new_row][new_col] == target:
            new_area, new_neighbors = get_regions(new_row, new_col, visited, target) 
            area += new_area
            neigbors += new_neighbors-1
    
    return area, neigbors


for row in range(rows):
    for col in range(cols):
        if (row, col) not in visited:
            target = lines[row][col]
            cur_area, cur_neigh = get_regions(row, col, visited, target)
            cost += cur_area*cur_neigh

print(cost)


