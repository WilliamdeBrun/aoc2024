filename = "input1.txt"

list1 = []
list2 = []

with open(filename, "r") as file:
    for line in file:
        id1, id2 = line.strip().split()
        list1.append(int(id1))
        list2.append(int(id2))

def get_sim_score(l1, l2):
    sim_score = 0
    for elem in l1:
        sim_score += elem * l2.count(elem)
    
    return sim_score

total_sim_score = get_sim_score(list1, list2)
print(total_sim_score)