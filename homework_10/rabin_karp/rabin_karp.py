import random


def rabin_karp(s, sub):
    m = len(sub)
    if m > len(s):
        return []
    if m == 0:
        return []
    q = 2**31 - 1
    x = random.randint(256, q - 1)
    hash_sub = 0
    x_m = 1
    for ch in sub:
        hash_sub *= x
        hash_sub %= q
        hash_sub += ord(ch)
        hash_sub %= q

        x_m *= x
        x_m %= q

    idx = 0
    hash_window = 0
    results = []
    for ch in s:
        hash_window *= x
        hash_window %= q
        if idx >= m:
            hash_window -= (ord(s[idx - m]) * x_m) % q
            hash_window += q
            hash_window %= q

        hash_window += ord(ch)
        hash_window %= q
        if idx >= m - 1 and hash_window == hash_sub:
            # ошибка линтера, поэтому noqa
            if s[idx - m + 1 : idx + 1] == sub:  # noqa: E203
                results.append(idx - m + 1)
        idx += 1
    return results
