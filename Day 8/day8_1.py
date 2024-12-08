with open("input_8.txt", "r") as file:
    lines = [list(line.strip()) for line in file.readlines()]
    
tot_locations = 0
rows = len(lines)
cols = len(lines[0])
locations = []

def is_valid(row, col):
    if 0 <= row < rows and 0 <= col < cols and (row, col) not in locations:
        locations.append((row, col))
        return True
    return False


def check_node(cur_row, cur_col, node_letter):
    sum_antis = 0
    for row in range(rows):
        for col in range(cols):
            if cur_row == row and cur_col == col:
                continue
            if lines[row][col] == node_letter:
                dist_r = cur_row-row
                dist_c = cur_col-col
                if is_valid(cur_row+dist_r, cur_col+dist_c):
                    sum_antis += 1
                if is_valid(cur_row-2*dist_r, cur_col-2*dist_c):
                    sum_antis += 1
                
    return sum_antis

for row in range(rows):
    for col in range(cols):
        if lines[row][col] != ".":
            tot_locations+=check_node(row, col, lines[row][col])

print(tot_locations)