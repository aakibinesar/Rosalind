def merge_sorted_arrays(A, B):
    '''Merges two sorted arrays A and B into a sorted array C.'''

    # Initialize variables.
    i, j = 0, 0
    C = []

    # Add the smallest item from A or B until one of the arrays runs out of items.
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    # Add on the additional items from the remaining array. (Only one will be nonempty)
    C += A[i:] + B[j:]

    return C


file = open('rosalind_mer.txt','r').readlines()

list1 = file[1]
list2 = file[3]

array_1 = [int(s) for s in list1.split(' ')]
array_2 = [int(s) for s in list2.split(' ')]

print(merge_sorted_arrays(array_1,array_2))

output_data = open('output.txt','w')
output_data.write(' '.join(map(str,merge_sorted_arrays(array_1,array_2))))