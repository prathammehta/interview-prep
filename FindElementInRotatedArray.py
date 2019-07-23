# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/

# [1,2,3,4,5,6,7,8]
# [7,8,1,2,3,4,5,6]
# [3,4,5,6,7,8,1,2]

def findPivotInArray(a):
	start = 0
	end = len(a) - 1
	mid = int((len(a) - 1)/2)
	while start < end:
		if mid == end or mid == start:
			return mid
		elif a[mid] > a[end]:
			start = mid
		elif a[start] > a[mid]:
			end = mid
		else:
			return -1
		pass
		mid = int((start + end - 1)/2)

def binarySearch(a, start, mid, end, item):
	# print(start, mid, end)
	if item == a[mid]:
		return mid
	elif end <= start:
		return -1
	elif item < a[mid]:
		return binarySearch(a, start, int((start + mid - 1)/2), mid - 1, item)
	elif item > a[mid]:
		return binarySearch(a, mid + 1, int((end + mid + 1)/2), end, item)


def findElementInArray(a, element):
	arraySplitPoint = findPivotInArray(a)
	indexOfElement = -1
	if arraySplitPoint == -1:
		indexOfElement = binarySearch(a, 0, int((len(a) - 1)/2),len(a) - 1,element)
	elif element > a[0]:
		indexOfElement = binarySearch(a, 0, int(arraySplitPoint/2), arraySplitPoint, element)
	else:
		indexOfElement = binarySearch(a, arraySplitPoint + 1, int((arraySplitPoint + len(a))/2), len(a) - 1, element)

	return indexOfElement
	
index = findElementInArray([1,2,3,4,5,6,7,8,9],10)
if index < 0:
	print('Not Found')
else:
	print(index)

