def reverse_complement(s):
    complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return (''.join([complements[c] for c in reversed(s)]))


def reverse_palindromes(s):
    results = []

    l = len(s)

    for i in range(l):
        for j in range(4, 13):
            if i + j > l:
                continue

            s1 = s[i:i+j]
            s2 = reverse_complement(s1)

            if s1 == s2:
                results.append((i + 1, j))

    return results


with open('rosalind_revp.txt','r') as file:
    content = file.read()

DNA = ''

for i in range(1,len(content.splitlines())):
    DNA += content.splitlines()[i]

results = reverse_palindromes(DNA)

print ("\n".join(['\t'.join(map(str, r)) for r in results]))