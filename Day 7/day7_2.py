from itertools import product

with open("input_7.txt", "r") as file:
    lines = [list(line.split(" ")) for line in file.readlines()]

cal_result = 0
values = []
numbers = []
for eq in lines:
    cur_nums = []
    for i in range(len(eq)):
        if i == 0:
            values.append(int(eq[i][:-1]))
        else:
            cur_nums.append(int(eq[i]))
    numbers.append(cur_nums)

def check_eq(nums, val, op):
    temp_val = nums[0]
    for i in range(len(nums)-1):
        if op[i] == "+":
            temp_val += nums[i+1]
        elif op[i] == "||":
            temp_val = temp_val*10**(len(str(nums[i+1]))) + nums[i+1]
        else:
            temp_val *= nums[i+1]
    return temp_val == val

for i in range(len(numbers)):
    ops = list(product(["+", "*", "||"], repeat=len(numbers[i])-1))
    for op in ops:
        if check_eq(numbers[i], values[i], op):
            cal_result += values[i]
            break
print(cal_result)