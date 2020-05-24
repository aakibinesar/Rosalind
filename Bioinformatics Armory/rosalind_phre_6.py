from Bio import SeqIO
from numpy import *
fastq = open('rosalind_phre.txt')

threshold = int(fastq.readline().rstrip())
records = list(SeqIO.parse(fastq, 'fastq'))

print (len([i for i in records if mean(i.letter_annotations['phred_quality']) < threshold]))