seq_list = []
stseq = ''
for line in open('rosalind_ba9e.txt'):
    stseq = line.rstrip()
    seq_list.append(stseq)

n = len(seq_list)
l = len(stseq)
comseq = ''
star = 0


for start in range(0,l-star):
    for length in range(star+1,l-start):
        comseq = stseq[start:start+length]
        for one in range(0,n):
            if seq_list[one].find(comseq) >-1:
                if one == n-1:
                    if length > star:
                        print(length,comseq)
                        star = length
            else:
                break