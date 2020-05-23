from Bio.Seq import Seq


file = open('rosalind_revc.txt','r').read().replace('\n','')

my_seq = Seq(file).reverse_complement()

print (my_seq)