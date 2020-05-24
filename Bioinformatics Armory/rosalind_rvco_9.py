from Bio import SeqIO

with open('rosalind_rvco.txt') as input_data, open('output.txt','w') as output_data:
    # Check if the dna sequence matches its complement, add #Trues to get the number.
    rev_comp_match = sum([str(dna.seq) == str(dna.reverse_complement().seq) for dna in SeqIO.parse(input_data, 'fasta')])
    print (rev_comp_match)