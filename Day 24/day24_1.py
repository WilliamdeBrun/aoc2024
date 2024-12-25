with open("input_24.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

blank_idx = lines.index("")
wires = {}
gates = {}
outputs = {}
for i in range(len(lines)):
    if i < blank_idx:
        wire = lines[i].split(": ")
        wires[wire[0]] = int(wire[1])
    elif i > blank_idx:
        out = lines[i].split(" -> ")[1]
        operation = lines[i].split(" -> ")[0]
        parts = operation.split(" ")
        op1 = parts[0]
        operator = parts[1]
        op2 = parts[2]
        gates[out] = (op1, operator, op2)

def operate(wire):
    if wire in wires:
        return wires[wire]
    op1, operator, op2 = gates[wire]
    if operator == "AND":
        wires[wire] = operate(op1) & operate(op2)
                
    elif operator == "OR":
        wires[wire] = operate(op1) | operate(op2)            
    else:
        wires[wire] = operate(op1) ^ operate(op2)       
    return wires[wire]    

for output in gates:
    if output.startswith("z"):
        outputs[output] = operate(output)
        
            

sorted_outputs = dict(sorted(outputs.items(), reverse=True))

print(int("".join(map(str, sorted_outputs.values())), 2))
