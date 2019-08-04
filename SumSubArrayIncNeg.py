# https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/

def find_sequence(arr, target_sum):
	map = {}
	sum = 0
	for index in range(len(arr)):
		sum = sum + arr[index]
		map[str(sum)] = index

	for stored_sum, stored_index in map.items():
		if str(int(stored_sum) - target_sum) in map:
			index_1 = map[str(stored_sum)]
			index_2 = map[str(int(stored_sum) - target_sum)]
			return arr[index_1:index_2 + 1] if index_1 < index_2 else arr[index_2:index_1 + 1] 


print(find_sequence([1, 4, 20, 3, 10, 5], 33))