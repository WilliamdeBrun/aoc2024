from functools import cache
with open("input_11.txt", "r") as file:
    stones =  [int(x) for x in file.read().split(" ")]

@cache
def blink(stone, it):
    if it == 0:
        return 1
    if stone == 0:
        return blink(1, it-1)
    string = str(stone)    
    if len(string) % 2 == 0:
        return blink(int(string[len(string)//2:]), it-1) + blink(int(string[:len(string)//2]), it-1)
    
    return blink(2024*stone, it-1)

rec_depth = 75
sum_stones = 0    
for stone in stones:
    sum_stones += blink(stone,rec_depth)

print(sum_stones)
