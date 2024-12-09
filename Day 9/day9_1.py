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
    for i in range(len(disk_layout)-1, -1, -1):
        if disk_layout[i] != ".":
            for j in range(len(disk_layout)):
                if i == j:
                    return disk_layout
                if disk_layout[j] == ".":
                    temp = "."
                    disk_layout[j] = disk_layout[i]
                    disk_layout[i] = temp
                    break
    return disk_layout

checksum = 0
dl_updated = swap_places(disk_layout)
for i in range(len(dl_updated)):
    if dl_updated[i] == ".":
        break
    checksum += i*dl_updated[i]


print(checksum)