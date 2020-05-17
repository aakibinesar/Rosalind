file = open("rosalind_ini5.txt","r")

content = file.readlines()
content = [x.strip() for x in content]

for i in range(0,1000):
		if i % 2 == 1:
			print (content[i])

file.close()