def lcs(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i0 = len(s1)
    j0 = len(s2)
    answer_chars = []
    while i0 != 0 and j0 != 0:
        if s1[i0 - 1] == s2[j0 - 1]:
            answer_chars.append(s1[i0 - 1])
            i0 -= 1
            j0 -= 1
        else:
            if dp[i0][j0] == dp[i0 - 1][j0]:
                i0 -= 1
            else:
                j0 -= 1

    return "".join(reversed(answer_chars))
