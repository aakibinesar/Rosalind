f = open("rosalind_splc.txt", "r")
str1 = f.read()
str1 = str1.replace("Rosalind_", "")
str1 = str1.replace("\n", "")
str1 = ''.join([i for i in str1 if not i.isdigit()])
intron = str1.split(">")
intron.remove("")
str = intron[0]
del intron[0]

for i in intron:
    str = str.replace(i, '')

cod = {
    'TTT': 'F',         'CTT': 'L',     'ATT': 'I',     'GTT': 'V',
    'TTC': 'F',         'CTC': 'L',     'ATC': 'I',     'GTC': 'V',
    'TTA': 'L',         'CTA': 'L',     'ATA': 'I',     'GTA': 'V',
    'TTG': 'L',         'CTG': 'L',     'ATG': 'M',     'GTG': 'V',
    'TCT': 'S',         'CCT': 'P',     'ACT': 'T',     'GCT': 'A',
    'TCC': 'S',         'CCC': 'P',     'ACC': 'T',     'GCC': 'A',
    'TCA': 'S',         'CCA': 'P',     'ACA': 'T',     'GCA': 'A',
    'TCG': 'S',         'CCG': 'P',     'ACG': 'T',     'GCG': 'A',
    'TAT': 'Y',         'CAT': 'H',     'AAT': 'N',     'GAT': 'D',
    'TAC': 'Y',         'CAC': 'H',     'AAC': 'N',     'GAC': 'D',
    'TAA': '',      'CAA': 'Q',     'AAA': 'K',     'GAA': 'E',
    'TAG': '',      'CAG': 'Q',     'AAG': 'K',     'GAG': 'E',
    'TGT': 'C',         'CGT': 'R',     'AGT': 'S',     'GGT': 'G',
    'TGC': 'C',         'CGC': 'R',     'AGC': 'S',     'GGC': 'G',
    'TGA': '',      'CGA': 'R',     'AGA': 'R',     'GGA': 'G',
    'TGG': 'W',         'CGG': 'R',     'AGG': 'R',     'GGG': 'G'
}

b = []
for i in range(0, len(str), 3):
    f = str[i:i+3]
    b.append(f)


c = ''.join(cod[i] for i in b)
print(c)