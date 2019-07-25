# https://www.geeksforgeeks.org/double-first-element-move-zero-end/

def rotateArray(arr, index):
	for index in range(index,len(arr) - 1):
		arr[index] = arr[index + 1]
		pass
	arr[len(arr) - 1] = 0

def doubleAndMoveToEnd(arr):
	numberOfZeroes = 0
	for index in range(0,len(arr)-1):
		if arr[index] != 0 and arr[index + 1] == arr[index]:
			arr[index] *= 2
			arr[index+1] = 0
			pass

		if arr[index] == 0:
			numberOfZeroes += 1
		pass

	print(numberOfZeroes)

	index = 0
	numberOfRotations = 0
	while numberOfRotations < numberOfZeroes:
		print(arr)
		if arr[index] == 0:
			rotateArray(arr, index)
			numberOfRotations += 1
		else:
			index += 1		

	return arr



print(doubleAndMoveToEnd([0, 2, 2, 2, 0, 6, 6, 0, 0, 8]))