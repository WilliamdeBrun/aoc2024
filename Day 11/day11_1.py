with open("input_11.txt", "r") as file:
    stones =  [int(x) for x in file.read().split(" ")]

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        string = str(stone)    
        if len(string) % 2 == 0:
            new_stones.append(int(string[len(string)//2:]))
            new_stones.append(int(string[:len(string)//2]))
        else:
            new_stones.append(2024*stone)
    return new_stones

for _ in range(25):
    stones = blink(stones)
    

print(len(stones))
