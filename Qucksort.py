def quicksort (arr):
    if len(arr) < 2:
        return arr
    else :
        pivet = arr[0]
        less = [i for in arr[1:] if i <= pivet]
        greater = [i for in arr[1:] if i >= pivet]
        return quicksort(less + pivet + greater)

print (quicksort([3, 1, 6, 2, 7, 5, 4]))