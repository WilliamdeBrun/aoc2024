#solution without using a cache

with open("input_11.txt", "r") as file:
    stones =  [int(x) for x in file.read().split(" ")]

def blink(stone, it, visited):
    if it == 0:
        return 1
    
    if (stone, it) in visited:
        return visited[(stone, it)]
    
    string = str(stone)
    if stone == 0:
        new_path = blink(1, it-1, visited)
        
    elif len(string) % 2 == 0:
        new_path = blink(int(string[len(string)//2:]), it-1, visited) + blink(int(string[:len(string)//2]), it-1, visited)
    
    else:
        new_path = blink(2024*stone, it-1, visited)
    visited[(stone, it)] = new_path
    return new_path

visited = {}
rec_depth = 75
sum_stones = 0    
for stone in stones:
    sum_stones += blink(stone,rec_depth, visited)

print(sum_stones)
