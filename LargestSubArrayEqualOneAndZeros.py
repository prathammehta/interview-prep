# https://www.geeksforgeeks.org/largest-subarray-with-equal-number-of-0s-and-1s/
# This program is half complete


def find_subarray(arr):

	sum_array = []
	sum = 0
	for index in range(len(arr)):
		if arr[index] == 0:
			sum -= 1
		else:
			sum += 1
		sum_array.append(sum)

	map = {}
	max_difference = 0
	sub_array_start = 0
	sub_array_end = 0
	for index in range(len(arr)):
		if sum_array[index] not in map:
			map[sum_array[index]] = index

	for index in range(len(sum_array) - 1, -1, -1):
		first_index = map[sum_array[index]]
		difference = index - first_index
		if difference > max_difference and difference > 0:
			max_difference = index - first_index
			sub_array_start = min(index, first_index)
			sub_array_end = max(index, first_index)

	print(max_difference)
	print(sub_array_start)
	print(sub_array_end)


	print(sum_array, map)


find_subarray([1, 0, 1, 1, 1, 0, 0])