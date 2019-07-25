
def sumSubseqWidths(A):
    sumOfWidths = 0
    A.sort()
    for index in range(0, len(A)):
        for internalIndex in range(index + 1, len(A)):
            sumOfWidths = sumOfWidths + pow(2,(internalIndex - index) - 1) * (A[internalIndex] - A[index])
    
    return sumOfWidths % (pow(10,9)+7)

print(sumSubseqWidths([5,69,89,92,31,16,25,45,63,40,16,56,24,40,75,82,40,12,50,62,92,44,67,38,92,22,91,24,26,21,100,42,23,56,64,43,95,76,84,79,89,4,16,94,16,77,92,9,30,13]))
