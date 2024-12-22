from collections import deque
from itertools import product
with open("input_21.txt", "r") as file:
    codes = file.read().splitlines()


numpad = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
          "4": (1, 0), "5": (1, 1), "6": (1, 2),
          "1": (2, 0), "2": (2, 1), "3": (2, 2),
          "0": (3, 1), "A": (3, 2)}

dirpad = {"^": (0, 1), "A": (0, 2),
          "<": (1, 0), "v": (1, 1), ">": (1, 2)}

dirs = [(1, 0, "v"), (-1, 0, "^"), (0, 1, ">"), (0, -1, "<")]


def find_paths(pad, code):
    paths = {}
    for pos1 in pad:
        for pos2 in pad:
            if pos1 == pos2:
                paths[(pos1, pos2)] = ["A"]
                continue

            queue = deque([(pad[pos1], "")])
            min_length = float("inf")
            pos_paths = []
        
            while queue:
                
                (row, col), path =  queue.popleft()
                for dir_r, dir_c, key in dirs:
                    new_row = row + dir_r
                    new_col = col + dir_c
                    if not (new_row, new_col) in pad.values():
                        continue
                    if min_length < len(path) + 1:
                            break
                    if (new_row, new_col) == pad[pos2]:
                        
                        pos_paths.append(path + key + "A")
                        min_length = len(path) + 1
                            
                    else:
                        queue.append(((new_row, new_col), path + key))
                else:
                    continue
                break
            paths[(pos1, pos2)] = pos_paths
    
    best_subpaths = [paths[(pos1, pos2)] for pos1, pos2 in zip("A" + code, code)]
    best_paths = ["".join(p) for p in product(*best_subpaths)]
    return best_paths

total_val = 0

for code in codes:
    first_code_paths = find_paths(numpad, code)
    second_code_paths = []
    for path in first_code_paths:
        second_code_paths += find_paths(dirpad, path)
    shortest = min(map(len, second_code_paths))
    second_code_paths = [path for path in second_code_paths if len(path) == shortest]
    
    third_code_paths = []
    for path2 in second_code_paths:
        third_code_paths += find_paths(dirpad, path2)
    shortest = min(map(len, third_code_paths))
    third_code_paths = [path for path in third_code_paths if len(path) == shortest]
    
    total_val += len(third_code_paths[0]) * int(code[:-1])
print(total_val)