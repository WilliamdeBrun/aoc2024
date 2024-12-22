with open("input_22.txt", "r") as file:
    initial_secrets = [int(secret) for secret in file.read().splitlines()]

def mix_prune(initial, secret):
    secret = secret ^ initial
    secret = secret % 16777216
    return secret

def get_sequence(secret, its):
    ones_digits = []
    price_changes = []
    prev_secret = secret
    for _ in range(its):
        new_secret = secret * 64
        secret = mix_prune(secret, new_secret)
        new_secret = secret//32
        secret = mix_prune(secret, new_secret)
        new_secret = secret * 2048
        secret = mix_prune(secret, new_secret)
        ones_digits.append(secret % 10) 
        price_changes.append(secret % 10 - prev_secret % 10)
        prev_secret = secret
    sub_sequences = {}
    for i in range(len(price_changes)-3):
        key = tuple(price_changes[i:i+4])
        if key in sub_sequences:
            continue
        sub_sequences[key] = ones_digits[i+3]

    return sub_sequences

digits = {}
for secret in initial_secrets:
    sub_seqs = get_sequence(secret, 2000)
    for sub_seq, val in sub_seqs.items():
        if sub_seq in digits:
            digits[sub_seq] += val
        else:
            digits[sub_seq] = val

max_key, max_value = max(digits.items(), key=lambda item: item[1])
print(max_value)

