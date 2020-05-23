with open('rosalind_inod.txt') as input_data, open('output.txt', 'w') as output_data:
    n = int(input_data.read().strip())
    print n-2
    output_data.write(str(n-2))