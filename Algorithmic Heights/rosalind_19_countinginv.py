def merge_sorted_arrays_counting_inversions(A, B):
    '''Merges two sorted arrays A and B into a sorted array C and counts the nmber of inversions.'''
    # Initialize variables.
    i, j = 0, 0
    count = 0
    C = []

    # Add the smallest item from A or B until one of the arrays runs out of items.
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            count += len(A) - i
            j += 1

    # Add on the additional items from the remaining array. (Only one will be nonempty)
    C += A[i:] + B[j:]

    return C, count


def merge_sort_inversion_count(A):
    '''Uses the merge sort algorithm to sort an array A and count inversions.'''
    # Trivially sorted if the length is <= 1.
    # Also, this is used in the process of breaking down the array before rebuilding it sorted.
    if len(A) <= 1:
        return A, 0

    # Get the midpoint of A.
    midpoint = len(A)//2

    # Use merge sort to sort the lower and upper halves of A.
    lower, lower_inv = merge_sort_inversion_count(A[:midpoint])
    upper, upper_inv = merge_sort_inversion_count(A[midpoint:])

    # Combine the sorted lower and upper halves.
    combined, combined_inv = merge_sorted_arrays_counting_inversions(lower, upper)

    return combined, lower_inv+upper_inv+combined_inv


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    input_data = open('rosalind_inv.txt','r').readlines()
    array_1 = input_data[1].strip().split()

    map_object = map(int,array_1)
    list_of_integers = list(map_object)

    # A = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]
    
    # Get the number of inversions.
    inversions = merge_sort_inversion_count(list_of_integers)

    # Print and save the answer.
    print (inversions[1])
    

if __name__ == '__main__':
    main()