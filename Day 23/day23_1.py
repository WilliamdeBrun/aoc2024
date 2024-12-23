with open("input_23.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


pairs = set()
for line in lines:
    pair = sorted(line.split("-"))
    pairs.add(tuple(pair))  

combinations = {}
def get_comb(first, second, combinations):
    if first.startswith("t"):
        if not first in combinations:
            combinations[first] = [second]
        else:
            combinations[first] += [second]
    return combinations
for pair in pairs:
    combinations = get_comb(pair[0], pair[1], combinations)
    combinations = get_comb(pair[1], pair[0], combinations)
tot=0
visited = set()
for comb in sorted(combinations):
    cur_comb = sorted(combinations[comb])
    for i in range(len(cur_comb)-1):
        for j in range(i+1, len(cur_comb)):
            
            if (cur_comb[i], cur_comb[j]) in pairs:
                sorted_comb = tuple(sorted((comb, cur_comb[i], cur_comb[j])))
                if sorted_comb not in visited:
                    tot += 1
                    visited.add(sorted_comb)

print(tot)
