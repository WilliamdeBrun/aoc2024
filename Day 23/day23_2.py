with open("input_23.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


pairs = set()
for line in lines:
    pair = sorted(line.split("-"))
    pairs.add(tuple(pair)) 

combinations = {}
def get_comb(first, second, combinations):
    if not first in combinations:
        combinations[first] = [second]
    else:
        combinations[first] += [second]
    return combinations
for pair in pairs:
    combinations = get_comb(pair[0], pair[1], combinations)
    combinations = get_comb(pair[1], pair[0], combinations)

longest = 0
longest_connections = set()
for comb in sorted(combinations):
    cur_comb = sorted(combinations[comb])
    for i in range(len(cur_comb)):
        candidate_connections = {comb}
        for j in range(len(cur_comb)):
            if i != j and all((x, cur_comb[j]) in pairs or (cur_comb[j], x) in pairs for x in candidate_connections):
                candidate_connections.add(cur_comb[j])
        if len(candidate_connections) > longest:
            longest_connections = candidate_connections
            longest = len(candidate_connections)
            
    
longest_sorted = sorted(longest_connections)
print(",".join(longest_sorted))
