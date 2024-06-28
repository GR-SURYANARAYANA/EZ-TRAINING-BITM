def kmp_search(s, p):
    def kmp_partial_match_table(p):
        lps = [0] * len(p)
        length = 0
        i = 1
        while i < len(p):
            if p[i] == p[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = kmp_partial_match_table(p)
    i = j = 0
    indices = []
    while i < len(s):
        if p[j] == s[i]:
            i += 1
            j += 1

        if j == len(p):
            indices.append(i - j)
            j = lps[j - 1]
        elif i < len(s) and p[j] != s[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return indices

s = 'ACAZACAZ'
p = 'ACAZ'
print(kmp_search(s, p))
