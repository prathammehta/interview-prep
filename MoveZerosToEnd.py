# https://www.geeksforgeeks.org/move-zeroes-end-array/

def rotateArrayRight(a, index):
	for j in range(index,len(a)-1):
		a[j] = a[j+1]
		pass
	a[len(a)-1] = 0

def moveZeroesToEnd(a):
	numberOfZeroes = 0
	for item in a:
		if item == 0:
			numberOfZeroes += 1
		pass

	print(numberOfZeroes)
	
	i = 0
	while i < len(a):
		if a[i] == 0 and i < (len(a) - numberOfZeroes):
			rotateArrayRight(a, i)
		else:
			i += 1
		pass
	
	print(a)


moveZeroesToEnd([1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0])

