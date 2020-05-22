with open('rosalind_hea.txt', 'r') as contents:
    n, A = contents.read().strip().split('\n')
    n = int(n)
    A = [int(a) for a in A.split(' ')]

def buildHeap(A):

    def checkHeap(heap, index):

        # index of parent. should map: 
        #1 to 0
        #2 to 0
        #3 to 1
        #4 to 1
        #5 to 2
        
        # get parent. make sure it doesn't 'wraparound':
        parent = max((index - 1)//2, 0)

        # swap if parent is smaller than child:
        if heap[parent] < heap[index]:
            tmp = heap[index]
            heap[index] = heap[parent]
            heap[parent] = tmp
            #check grandparent etc. as well:
            checkHeap(heap, parent)

        # base case: don't need to swap
        else:
            pass

    heap = []
    # putting all the elements into the heap:
    while len(A) != 0:

        heap.append(A.pop(0))

        if len(heap) != 0:
            #'sift' up, using the recursive checkHeap function:
            checkHeap(heap, len(heap) -1)

    return heap


heap = buildHeap(A)

#print ' '.join([str(h) for h in heap])

with open('output.txt', 'w') as output:
    output.write(' '.join([str(h) for h in heap]))