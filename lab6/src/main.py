def Knutt_Morris_Pratt(haystack, needle):
    T = [0 for _ in range(len(needle))]
    T[0] = -1
    T[1] = 0
    j = 0
    for i in range(2, len(needle)):
        while j > 0 and needle[i - 1] != needle[j]:
            j = T[j]
        if needle[i - 1] == needle[j]:
            j += 1
        T[i] = j

    i = 0
    m = 0
    while m + i < len(haystack):
        if needle[i] == haystack[m + i]:
            if i == len(needle) - 1:
                return m
            i += 1
        else:
            m = m + i - T[i]
            if T[i] > -1:
                i = T[i]
            else:
                i = 0

    return len(haystack)
