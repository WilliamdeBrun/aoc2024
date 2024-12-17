with open("input_17.txt", "r") as file:
    lines = file.readlines()

A = 0
B = 0
C = 0
prog = []

for line in lines:
    if line.startswith("Register A"):
        A = int(line.split(":")[1])
        
    elif line.startswith("Register B"):
        B = int(line.split(":")[1])

    elif line.startswith("Register C"):
        C = int(line.split(":")[1])
        
    elif line.startswith("Program"):
        x = line.split(": ")[1]
        for num in x.split(","):
            prog.append(int(num))
        
def get_A(a, b=0, c=0):
    def get_combo(operand):
        if operand < 4:
            return operand
        else:
            if operand == 4:
                return a
            elif operand == 5:
                return b
            elif operand == 6:
                return c

    i = 0
    output = []
    while i < len(prog):
        op = prog[i+1]
        inst = prog[i]
        if inst == 0:
            a = a//(2**get_combo(op)) #adv
        elif inst == 1:
            b = op ^ b #bxl
        elif inst == 2:
            b = get_combo(op) % 8 # bst
        elif inst == 3:
            if a != 0:
                i = op #jnz
                continue
        elif inst == 4:
            b = b ^ c # bxc
        elif inst == 5:
            val = get_combo(op) % 8
            output.append(val) #out
        elif inst == 6:
            b = a//(2**get_combo(op)) #bdv
        else:
            c = a//(2**get_combo(op)) #cdv
        
        i += 2
    
    return output
posible_As = [0]

for i in range(len(prog)):
    new_As = []
    for pa in posible_As:
        for j in range(8):
            temp = pa * 8 + j
            if get_A(temp) == prog[-i-1:]:
                new_As.append(temp)
    posible_As = new_As

best_A = min(posible_As)
    
print(best_A)