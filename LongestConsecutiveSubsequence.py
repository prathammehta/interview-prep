# https://www.geeksforgeeks.org/printing-longest-increasing-consecutive-subsequence/

def longest_subseq(arr):
	map = {}
	for index in range(len(arr)-1, -1, -1):
		
		if (arr[index] + 1) in map:
			map[arr[index]] = map[arr[index] + 1] + 1

		else:
			map[arr[index]] = 1

	max_key = 0
	max_length = 0
	for key,value in map.items():
		if value > max_length:
			max_length = value
			max_key = key


	for index in range(max_key, max_key + max_length):
		print(index, end=' ')

	print('')

longest_subseq([6, 7, 8, 3, 4, 5, 9, 10])