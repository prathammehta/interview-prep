# https://www.geeksforgeeks.org/printing-maximum-sum-increasing-subsequence/

def get_subsequence(arr):
	l = len(arr)
	max_sum = [arr[i] for i in range(l)]
	max_sum_seq = [[arr[i]] for i in range(l)]
	

	for i in range(1,l):
		max_value = 0
		max_index = 0
		for j in range(0,i):
			if arr[j] < arr[i] and max_value < max_sum[j]:
				max_value = max_sum[j]
				max_index = j
		max_sum[i] = max_value + arr[i]
		max_sum_seq[i] = max_sum_seq[max_index] + max_sum_seq[i]
	

	return max_sum_seq[max_sum.index(max(max_sum))]

print(get_subsequence([1, 101, 2, 3, 100, 4, 5]))