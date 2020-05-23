import math

def binomial(n, i, j):
    return (math.factorial(n) / math.factorial(i) / math.factorial(n-i)) * ((j/n)**i * (1-(j/n))**(n-i))

def probability(n, m, g, k):
    
    n = n * 2

    current = [0 for i in range(n+1)]
    current[m] = 1
    
    for z in range (g):

        next = [0 for i in range(n+1)]
        
        for i in range(n+1):
            for j in range(n+1):
                next[i] = next[i] + binomial(n, i, j) * current[j]
                
        current = next

    return round(sum(current[:-k]),3)
       
print(probability(6, 10, 5, 6))