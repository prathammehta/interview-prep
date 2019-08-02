import sys

def find_minimum_steps(arr, i):
	if arr[i] + 1 > len(arr):
		return 0

	else:
		min_value = sys.maxsize
		for index in range(1, min(arr[i]+1,len(arr)-i)):
			value = find_minimum_steps(arr, i+index) + 1
			if value < min_value:
				min_value = value

		return min_value

print(find_minimum_steps([1,2,3,4,5], 0))