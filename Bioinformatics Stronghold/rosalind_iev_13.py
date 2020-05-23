f = open("rosalind_iev.txt", "r")
f = f.readline()
b = f.split(" ")
bint = []
for i in range (0, len(b)):
    bint.append(int(b[i]))

def expected (a):
    sum = (a[0] * 1 + a[1] * 1 + a[2] * 1 + a[3] *0.75 + a[4] *0.5 + a[5] * 0) * 2
    return sum

print(expected(bint))