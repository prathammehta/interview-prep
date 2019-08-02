# https://www.geeksforgeeks.org/longest-repeated-subsequence/

def longest_repeated_subsequence(string, n):
	lrs = [[0 for _ in range(n+1)] for _ in range(n+1)]

	for i in range(1,n + 1):
		for j in range(1,n + 1):
			if string[i-1] == string[j-1] and i != j:
				lrs[i][j] = lrs[i-1][j-1]+1
			else:
				lrs[i][j] = max(lrs[i][j-1], lrs[i-1][j])

	i = n
	j = n
	sequence = ''
	
	while i>0 and j>0:
		if lrs[i][j] == lrs[i-1][j-1] + 1:
			sequence += string[i-1]
			i -= 1
			j -= 1
		elif lrs[i-1][j] == lrs[i][j-1]:
			i -= 1
		else:
			j -= 1


	return sequence[::-1]

a = 'aabebcdd'
print(longest_repeated_subsequence(a, len(a)))

