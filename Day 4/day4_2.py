with open("input_4.txt", "r") as file:
    input = [list(line.strip()) for line in file.readlines()]

neighbors = [(-1, -1), (1, 1), (-1, 1),  (1, -1)]
rows = len(input)
cols = len(input[0])
count = 0
valid_letters = ["MSMS", "SMSM", "SMMS", "MSSM"]
def search_word(row, col):
    letters = ""
    for n in neighbors:
        new_row = row + n[0]
        new_col = col + n[1]
        if 0 <= new_row < rows and 0 <= new_col < cols:
            letters += input[new_row][new_col]
        
    return letters in valid_letters

for row in range(rows):
    for col in range(cols):
        if input[row][col] == "A" and search_word(row, col):
                count += 1

print(count)
