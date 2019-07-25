# https://www.youtube.com/watch?v=nqlNzOcnCfs

numberOfSeqs = 0

def calculateSum(arr, sum, target):
	global numberOfSeqs
	if sum == target:
		numberOfSeqs += 1
		return
	elif sum > target:
		return
	elif len(arr) == 0:
		return
	else:
		length = len(arr)
		for index in range(0,length):
			element = arr[0]
			arr.remove(element)
			calculateSum(
				arr.copy(), 
				sum + element, 
				target)


calculateSum([1,2,3,4,5,6,7,8], 0, 8)
print(numberOfSeqs)