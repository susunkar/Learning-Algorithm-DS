def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    newarry = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newarry.append(arr.pop(smallest))
    return newarry


print(selectionsort([5, 3, 6, 2, 10]))
