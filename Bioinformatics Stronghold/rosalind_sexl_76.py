with open('rosalind_sexl.txt') as f:
    sex = map(float, f.readline().strip().split())
    
prob = [i * (1-i) / 0.5 for i in sex]
    
print(' '.join([str(i) for i in prob]))