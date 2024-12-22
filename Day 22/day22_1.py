with open("input_22.txt", "r") as file:
    initial_secrets = [int(secret) for secret in file.read().splitlines()]

def mix_prune(initial, secret):
    secret = secret ^ initial
    secret = secret % 16777216
    return secret

def new_secret(secret, its):
    for _ in range(its):
        new_secret = secret * 64
        secret = mix_prune(secret, new_secret)
        new_secret = secret//32
        secret = mix_prune(secret, new_secret)
        new_secret = secret * 2048
        secret = mix_prune(secret, new_secret)
    return secret


total = sum(new_secret(secret, 2000) for secret in initial_secrets)

print(total)