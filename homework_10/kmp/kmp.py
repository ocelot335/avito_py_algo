def prefix_f(s):
    pi = [0] * len(s)
    k = 0

    for i in range(1, len(s)):
        while k > 0 and s[i] != s[k]:
            k = pi[k - 1]
        if s[i] == s[k]:
            k += 1
        pi[i] = k

    return pi


def kmp(s, sub):
    pi = prefix_f(sub)
    m = len(sub)
    if m == 0:
        return []
    k = 0
    results = []
    for i in range(len(s)):
        while k > 0 and s[i] != sub[k]:
            k = pi[k - 1]
        if s[i] == sub[k]:
            k += 1
        if k == m:
            results.append(i - m + 1)
            k = pi[k - 1]

    return results
