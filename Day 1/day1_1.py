filename = "input1.txt"

list1 = []
list2 = []

with open(filename, "r") as file:
    for line in file:
        id1, id2 = line.strip().split()
        list1.append(int(id1))
        list2.append(int(id2))

def get_distance(l1, l2):
    distances = []
    l1.sort()
    l2.sort()
    for i in range(len(l1)):
        distances.append(abs(l1[i]-l2[i]))
    
    return sum(distances)

total_distance = get_distance(list1, list2)
print(total_distance)
    