with open("input_17.txt", "r") as file:
    lines = file.readlines()

A = 0
B = 0
C = 0
prog = []
output = []
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

    
def get_combo(operand):
    if operand < 4:
        return operand
    else:
        if operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
i = 0
while i < len(prog):
    op = prog[i+1]
    inst = prog[i]
    if inst == 0:
        A = A//(2**get_combo(op)) 
    elif inst == 1:
        B = op ^ B
    elif inst == 2:
        B = get_combo(op) % 8
    elif inst == 3:
        if A != 0:
            i = op
            continue
    elif inst == 4:
        B = B ^ C
    elif inst == 5:
        val = get_combo(op) % 8
        output.append(val)
    elif inst == 6:
        B = A//(2**get_combo(op))
    else:
        C = A//(2**get_combo(op))
    
    i += 2

    
print(*output, sep=",")