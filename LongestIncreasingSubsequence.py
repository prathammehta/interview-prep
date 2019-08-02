# https://www.geeksforgeeks.org/longest-increasing-subsequence-dp-3/

def longest_increasing_subsequence(arr):
	lis = [1] * len(arr)

	for i in range(1,len(arr)):
		max_lis = 1
		for j in range(0,i):
			if arr[j] < arr[i] and (lis[j]+1) > max_lis:
				max_lis = lis[j] + 1
		lis[i] = max_lis

	print(lis)

longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80, 2])

