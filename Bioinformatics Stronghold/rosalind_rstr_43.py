def probability (n, x, s):
    p = 1
    at = 0
    gc = 0
    for i in s:
        if i == 'A' or i == 'T':
            at = at + 1
        elif i == 'G' or i == 'C':
            gc = gc + 1

    q = ((0.5*x) ** gc) * ((0.5 - 0.5*x) ** at) 
    p = 1 - (1 - q) ** n
    return p


print(round(probability(94758, 0.406321, 'AGATTCACG'),3))