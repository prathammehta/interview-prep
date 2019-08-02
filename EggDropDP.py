# https://www.geeksforgeeks.org/egg-dropping-puzzle-dp-11/
import sys

map = {}

def egg_count(n, k):
	global map
	key = str(n) + '-' + str(k)
	if key in map:
		return map[key]
	if k == 1:
		map[key] = n
		return n
	if n == 1:
		map[key] = 1
		return 1
	if n < 1:
		map[key] = 0
		return 0

	min_value = sys.maxsize
	for index in range(1,n+1):
		value = max(egg_count(index-1, k-1) + 1, egg_count(n-index, k) + 1)
		if value < min_value:
			min_value = value
		pass
	map[key] = min_value
	return min_value


def egg_count_bu(n,k):

	count = [[0 for i in range(k+1)] for j in range(n+1)]
	for i in range(1,n+1):
		count[i][1] = i

	for i in range(1, k+1):
		count[1][i] = 1

	for i in range(2,n+1):
		for j in range(2,k+1):
			min_value = sys.maxsize
			for l in range(1, i+1):
				value = max(count[l-1][j-1], count[i-l][j]) + 1
				if min_value > value:
					min_value = value
			count[i][j] = min_value

	return count[n][k]

print(egg_count_bu(100, 2))

