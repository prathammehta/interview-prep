def countPartitions(n, max_used,seq):
	if n < 0:
		return 0

	if n == 0:
		print(seq)
		return 1

	ways = 0
	for i in range(max_used,n + 1):
		ways += countPartitions(n - i, i, seq + [i])

	return ways





print(countPartitions(7,1, []) - 1)