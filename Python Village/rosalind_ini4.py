input_data = open('data/python/rosalind_ini4.txt','r')
	a,b = map(int, input_data.read().strip().split())

if a % 2 == 0:
	a += 1

c = 0
for i in range(a, b+1, 2):
	c += i

print c
