with open("input_24.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

blank_idx = lines.index("")
wires = {}
gates = {}
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

io_wires = ["x", "y", "z"]
wrong_ops = set()
for out in gates.keys():
    op1, operator, op2 = gates[out]
    if out[0] == "z" and operator != "XOR" and out != "z45":
        wrong_ops.add(out)
    if operator == "XOR" and out[0] not in io_wires and op1[0] not in io_wires and op2[0] not in io_wires:
        wrong_ops.add(out)
    if operator == "AND" and "x00" not in [op1, op2]:
        for subout in gates.keys():
            subop1, suboperator, subop2 = gates[subout]
            if (out == subop1 or out == subop2) and suboperator != "OR":
                wrong_ops.add(out)
    if operator == "XOR":
        for subout in gates.keys():
            subop1, suboperator, subop2 = gates[subout]
            if (out == subop1 or out == subop2) and suboperator == "OR":
                wrong_ops.add(out)
print(",".join(sorted(wrong_ops)))

