#python2
input_data = open('data/python/rosalind_ini3.txt','r')
	s, points = [line.strip() for line in input_data.readlines()]
	a,b,c,d = map(int, points.split())

slices = [s[a:b+1], s[c:d+1]]

print ' '.join(slices)

