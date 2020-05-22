with open('rosalind_hs.txt', 'r') as contents:
	n, A = contents.read().strip().split('\n')
	n = int(n)
	A = [int(a) for a in A.split(' ')]

def heapSort(A):

	def buildHeap(A):

		def checkHeap(heap, index):

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

	def sortHeap(heap):
		def siftDown(heap, index):

			length = len(heap)
			left_child = 2*index + 1
			right_child = 2*index + 2

			#children:
			children = []

			if left_child >= length:
				left_child = None
			else:
				children.append(left_child)

			if right_child >= length:
				right_child = None
			else:
				children.append(right_child)

			# if both are None, i.e. a base case:
			if not children:
				return

			# get the index of the larger child:
			to_swap = max(children, key = lambda x: heap[x])

			# if the parent is smaller than the child, do a swap:
			if heap[index] < heap[to_swap]:
				tmp = heap[index]
				heap[index] = heap[to_swap]
				heap[to_swap] = tmp

				#check again to see if the element needs to be sifted down again:
				siftDown(heap, to_swap)
			else:
				return

		sorted_arr = []

		while heap:
			#swap elements of the beginning and last element:
			tmp = heap[0]
			heap[0] = heap[-1]
			heap[-1] = tmp

			#prepend to sorted list:
			sorted_arr.insert(0, heap.pop())

			# recursively sift the first element down:
			siftDown(heap, 0)

		return sorted_arr

	heap = buildHeap(A)
	return sortHeap(heap)

sorted_A = heapSort(A)

with open('output.txt', 'w') as output:
	output.write(' '.join([str(s) for s in sorted_A]))