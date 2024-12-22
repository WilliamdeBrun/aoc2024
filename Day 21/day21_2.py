from collections import deque
from itertools import product
from functools import cache
with open("input_21.txt", "r") as file:
    codes = file.read().splitlines()


numpad = {"7": (0, 0), "8": (0, 1), "9": (0, 2),
          "4": (1, 0), "5": (1, 1), "6": (1, 2),
          "1": (2, 0), "2": (2, 1), "3": (2, 2),
          "0": (3, 1), "A": (3, 2)}

dirpad = {"^": (0, 1), "A": (0, 2),
          "<": (1, 0), "v": (1, 1), ">": (1, 2)}

dirs = [(1, 0, "v"), (-1, 0, "^"), (0, 1, ">"), (0, -1, "<")]


def find_paths(pad):
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
    return paths

def find_num_path_by_code(paths, code):
    best_subpaths = [paths[(pos1, pos2)] for pos1, pos2 in zip("A" + code, code)]
    best_paths = ["".join(p) for p in product(*best_subpaths)]
    return best_paths

numpad_paths = find_paths(numpad)
dirpad_paths = find_paths(dirpad)

@cache
def get_path_len(n_robots, pos1, pos2):
    if n_robots == 0:
        return len(dirpad_paths[(pos1, pos2)][0])
    shortest = float("inf")
    for path in dirpad_paths[(pos1, pos2)]:
        tot_len = 0
        for pos3, pos4 in zip("A" + path, path):
            tot_len += get_path_len(n_robots-1, pos3, pos4)
        shortest = min(shortest, tot_len)
    return shortest

total_val = 0

for code in codes:
    num_code_paths = find_num_path_by_code(numpad_paths, code)
    shortest = float("inf")
    for path in num_code_paths:
        tot_len = 0
        for pos1, pos2 in zip("A" + path, path):
            tot_len += get_path_len(24, pos1, pos2)
        shortest = min(shortest, tot_len)
    total_val += shortest * int(code[:-1])
                         
print(total_val)