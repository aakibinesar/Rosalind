from Bio import Entrez
from Bio import SeqIO

with open('rosalind_frmt.txt') as input_data:
    IDs = input_data.read().strip().split()

Entrez.email = 'aakib.nesar@gmail.com'
handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))

[min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]

handle2 = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
minFASTA = handle2.read().strip().split('\n\n')[min_index]

print (minFASTA)
with open('output.txt', 'w') as output_data:
    output_data.write(minFASTA)