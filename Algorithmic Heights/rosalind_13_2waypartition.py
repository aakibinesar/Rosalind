import sys

f = open('rosalind_par.txt')
lines = f.read().split('\n')
f.close()

n = int(lines[0])
arrayA = lines[1].split()
for x in range(0, n):
    arrayA[x] = int(arrayA[x])

pivot = arrayA[0]
arrayB = []
arrayB.append(pivot) 
positionPivot = 0

def addElement(pivot, element, array, positionPivot):
    if element > pivot:
        array.append(element)
        return array
    elif element < pivot:
        positionPivot += 1
        return [element] + array
    else: # Same value as the pivot
        left = array[:positionPivot]
        right = array[positionPivot:]
        return left + [pivot] + right

for element in arrayA[1:]:
    temp = addElement(pivot, element, arrayB, positionPivot)
    arrayB = temp

for element in arrayB:
    sys.stdout.write(str(element) + ' ')
print('')