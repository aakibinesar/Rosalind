from Bio.Seq import Seq

file = open('rosalind_ini.txt','r').read().replace('\n','')

my_seq = Seq(file)

print (my_seq.count("A"), my_seq.count("C"), 
	my_seq.count("G"), my_seq.count("T"))