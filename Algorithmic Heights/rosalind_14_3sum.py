f = open('rosalind_3sum.txt')
files = f.read()
files = files.split('\n')
files0 = files[0].split()

k = int(files0[0]) #number of arrays
n = int(files0[1]) #array length


for x in range(1, k+1):
    found = False
    line = files[x]
    line = line.split()

    # Make hash table with all numbers in the thing
    numbers = {}
    for i in range(0, n):
        numbers[int(line[i])] = i

    for a in range(0, n):
        if found == True:
            break
        else:
            first = int(line[a])
        for b in range(a+1, n):
            second = int(line[b])
            if ((-1)*(first+second)) in numbers:
                c = numbers[(-1)*(first+second)]
                print(str(a+1) + ' ' + str(b+1) + ' ' + str(c+1))
                found = True
                break 
    if found == False:
        print ('-1')