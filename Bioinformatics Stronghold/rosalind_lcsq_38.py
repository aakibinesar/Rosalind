f = open("rosalind_lcsq.txt", "r")
mat = []
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
mat = str1.split(">")
mat.remove("")

S, T = mat
ssm = [''] * (len(T) + 1) 
for i in S:
    last = ssm
    ssm = [''] 
    for j, k in enumerate(T):
        if(i == k):
            ssm.append(last[j] + i)
        else:
            ssm.append(max(last[j+1], ssm[-1], key=len))
print (ssm[-1])