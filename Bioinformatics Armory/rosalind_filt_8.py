from Bio import SeqIO
fastq = open('rosalind_filt.txt')

#t = threshold, p = percentage
t,p = [int(i) for i in fastq.readline().rstrip().split()]
records = list(SeqIO.parse(fastq,'fastq'))

#q = phredQuality list
q = [record.letter_annotations['phred_quality'] for record in records]

print (len([k for k in [sum([int(j >= t) for j in i])/float(len(i)) for i in q] if k >= p/100.]))