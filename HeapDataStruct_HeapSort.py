def buildHeap(A):
    n = len(A)
    for i in range(int(n/2-1),-1,-1):
        heapify(A,i,n)

def heapify(A, idx, maxIdx):
    left = 2 * idx + 1
    right = 2* maxIdx +1
    if left <maxIdx and A[left] > A[idx]:
        largest = left
    else:
        largest = idx

    if right <maxIdx and A[right]>A[largest]:
        largest = right

    if largest != idx:
        temp = A[largest]
        A[largest]= A[idx]
        A[idx] = temp
        heapify(A, largest, maxIdx)

def heapSort (A):
    buildHeap(A)
    for i in range(len(A)-1, 0, -1 ):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heapify(A,0,i)