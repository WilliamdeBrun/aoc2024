
with open("input2.txt", "r") as file:
    reports = [line.strip().split() for line in file.readlines()]
   

def is_safe(report):
    inc = True
    dec = True
    for i in range(len(report)-1):

        diff = int(report[i]) - int(report[i+1])
        if diff < 1 or diff > 3:
            inc = False
        if diff > -1 or diff < -3:
            dec = False
    return dec or inc

safe_reports = 0

for report in reports:
    if is_safe(report):
        safe_reports += 1
        
    


print(safe_reports)
