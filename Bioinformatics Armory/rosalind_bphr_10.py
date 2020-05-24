from Bio import SeqIO
from numpy import *

fastq = open('rosalind_bphr.txt')
threshold = int(fastq.readline().rstrip())
records = list(SeqIO.parse(fastq,'fastq'))

phredQuality = [record.letter_annotations['phred_quality'] for record in records]
#phredQuality = []
#for record in records:
#    phredQuality.append(record.letter_annotations['phred_quality'])

print (len([k for k in [mean([i[j] for i in phredQuality]) for j in range(len(phredQuality[0]))] if k < threshold]))