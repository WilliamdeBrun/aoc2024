with open('input_25.txt', 'r') as file:
    grids = file.read().strip().split('\n\n') 

locks = []
keys = []

for grid in grids:
    rows = grid.split('\n')
    if all(char == '#' for char in rows[0]):
        locks.append(rows)
    else:
        keys.append(rows)

locks_as_heights = []
keys_as_heights = []

for lock in locks:
    columns = zip(*lock)
    column_heights = [sum(1 for char in column if char == '#') for column in columns]
    locks_as_heights.append(column_heights)

for key in keys:
    columns = zip(*key)
    column_heights = [sum(1 for char in column if char == '#') for column in columns]
    keys_as_heights.append(column_heights)

n_pairs = 0
for lh in locks_as_heights:
    for kh in keys_as_heights:
        if all(lh[i] + kh[i] <= 7 for i in range(len(lh))):
            n_pairs += 1
print(n_pairs)
        