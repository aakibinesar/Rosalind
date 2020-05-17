str = open('rosalind_ini6.txt','r').read().replace('\n','')

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for key, value in counts.items():
    	print (key, value)

word_count(str)