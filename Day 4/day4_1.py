with open("input_4.txt", "r") as file:
    input = [list(line.strip()) for line in file.readlines()]

neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
rows = len(input)
cols = len(input[0])
word = "XMAS"
wordlength = len(word)
count = 0

def search_word(row, col, neigh_row, neigh_col):
    curr_word = ""
    for i in range(wordlength):
        new_row = row + i * neigh_row
        new_col = col + i * neigh_col
        if 0 <= new_row < rows and 0 <= new_col < cols:
            curr_word += input[new_row][new_col]
    return curr_word == word

for row in range(rows):
    for col in range(cols):
        for x, y in neighbors: 
            if search_word(row, col, y, x):
                count += 1

print(count)
