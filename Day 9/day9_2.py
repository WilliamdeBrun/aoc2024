with open("input_9.txt", "r") as file:
    chars = list(file.read())

letters = [char for char in chars if char.strip()]

disk_layout = []
curr_id = 0
for i in range(len(letters)):
    val = int(letters[i])
    for j in range(val):
        if i % 2 == 0:
            disk_layout.append(curr_id)
            if j == val-1:
                curr_id += 1
        else:
            disk_layout.append(".")

def swap_places(disk_layout):
    i = len(disk_layout)-1
    while (i > 0):
        if disk_layout[i] != ".":
            
            repeats = 1
            for k in range(1, 9):
                if i -k >= 0 and disk_layout[i-k] == disk_layout[i]:
                    repeats += 1
                else:
                    break 
            for j in range(len(disk_layout) - repeats +1):
                if j + repeats - 1 == i:
                    i = i - repeats + 1
                    break
                curr_seg = disk_layout[j:j+repeats]
                if all(x == "." for x in curr_seg):
                    for m in range(repeats):
                        disk_layout[j+m] = disk_layout[i-repeats + m + 1]
                        disk_layout[i-repeats +1 +m] = "."
                    break
        i -= 1
                    
    return disk_layout

checksum = 0
dl_updated = swap_places(disk_layout)
for i in range(len(dl_updated)):
    if dl_updated[i] == ".":
        continue
    checksum += i*dl_updated[i]
print(checksum)