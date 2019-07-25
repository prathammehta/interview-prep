# https://www.geeksforgeeks.org/rearrange-positive-and-negative-numbers/

def rotateArray(arr, start, end):
	temp = arr[end]
	for i in range(end - 1, start - 1, -1):
		arr[i + 1] = arr[i]
	arr[start] = temp

def rearrangePosNeg(arr):
	positionOfEarliestNeg = -1
	for index in range(0,len(arr)):
		print(arr)
		if positionOfEarliestNeg == -1 and arr[index] < 0:
			positionOfEarliestNeg = index
		elif positionOfEarliestNeg >= 0 and arr[index] >= 0:
			rotateArray(arr, positionOfEarliestNeg, index)
			positionOfEarliestNeg += 1

	return(arr)

print(rearrangePosNeg([12, 11, -13, -5, 6, -7, 5, -3, -6]))



