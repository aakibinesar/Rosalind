def linearSearch( bigArray, k ):
    return sorted(bigArray, reverse=False)[:k]

def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('rosalind_ps.txt') as input_data:
        input_data.readline()  # Skip first line.
        a = map(int, input_data.readline().strip().split())

    fileHandle = open ('rosalind_ps.txt')
    lineList = fileHandle.readlines()
    fileHandle.close()
    l = int(lineList[-1])

    # Quicksort array a.
    b = linearSearch(a,l)

    # Print and save the answer.
    print ' '.join(map(str,b))
    with open('output.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,a)))

if __name__ == '__main__':
    main()