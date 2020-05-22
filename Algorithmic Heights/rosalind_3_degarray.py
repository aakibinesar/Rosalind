file = open('rosalind_deg.txt','r').readlines()

vertices, edges = (int(val) for val in file[0].split())

my_data = [[int(val) for val in line.split()] for line in file[1:]]

count = 0

L = []


for k in range(1,vertices+1):
	count = 0
	for i in range(2):
		for j in range(0,edges):
			if my_data[j][i] == k:
				count+=1
	L.append(count)		

print(' '.join(str(num) for num in L))