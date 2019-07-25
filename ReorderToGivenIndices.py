# https://www.geeksforgeeks.org/reorder-a-array-according-to-given-indexes/

def reorderArray(arr, ind):
    n = len(ind)
    for i in range(n):
        for j in range(0, n-i-1):
            if ind[j] > ind[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ind[j], ind[j+1] = ind[j+1], ind[j]

    print(arr)
    print(ind)

reorderArray([50, 40, 70, 60, 90], [3,  0,  4,  1,  2])