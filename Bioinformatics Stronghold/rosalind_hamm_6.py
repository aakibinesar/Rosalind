file = open('rosalind_hamm.txt','r').readlines()

str1 = file[0].replace('\n','')
str2 = file[1].replace('\n','')

count = 0

length = len(str1)

for x in range(length):
	
	if str1[x]!= str2[x]:
		count+=1

print(count)