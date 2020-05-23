from math import factorial

def comb (a, b):
        return factorial(a) // (factorial(b) * factorial(a - b))

m = 1994
n = 1307
sum = 0
    
for i in range(n, m + 1):
    sum = sum + comb(m, i)

print (sum % 1000000)