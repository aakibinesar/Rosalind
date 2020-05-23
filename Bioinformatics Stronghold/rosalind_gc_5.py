from Bio.Seq import Seq


file = open('rosalind_gc.txt','r').readlines()

file_length = len(file)

L1 = []
L2 = []
prob_result = []


for i in range(file_length):

	if i % 2 == 0:
		L1.append(file[i])

	if i % 2 == 1:
		L2.append(str(file[i]).replace(' ','').replace('\n',''))

	

print(L2)
L2_length = len(L2)

for x in range(L2_length):

	 my_seq = Seq(L2[x])
	 

	 DNA_string_len = len(L2[x])
	 

	 countC = my_seq.count('C')
	 
	 countG = my_seq.count('G')
	 

	 Prob = (((countC + countG)) / DNA_string_len) * (pow(10,2))
	 prob_result.append(Prob)



index = prob_result.index(max(prob_result))

print (str(L1[index]).replace('>','').replace('\n',''))
print(max(prob_result))