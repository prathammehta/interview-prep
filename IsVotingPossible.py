# https://www.geeksforgeeks.org/check-people-can-vote-two-machines/

def can_we_vote(a, index, t1, t2):
	if t1 < 0 or t2 < 0:
		return 0
	if t1 <= 0 and t2 <= 0 and index < len(a):
		return 0
	if index >= len(a):
		return 1
	if t1 == 0:
		return can_we_vote(a, index+1, 0, t2-a[index])
	if t2 == 0:
		return can_we_vote(a, index+1, t1-a[index], 0)

	return max(can_we_vote(a, index+1, t1 - a[index], t2), can_we_vote(a, index+1, t1, t2 - a[index]))

def can_we_vote_dp(a, t):
	n = len(a)
	times = [[0 for _ in range(n)] for _ in range(2)]
	times[0][0] = a[0]
	times[1][0] = a[1]
 
	i = 1
	j = 1

	for index in range(2,n):
		if times[0][i-1] < times[1][j-1]:
			times[0][i] = times[0][i-1] + a[index]
			i += 1
			if times[0][i-1] > t:
				return 0
		else:
			times[1][j] = times[0][j-1] + a[index]
			j += 1
			if times[1][j-1] > t:
				return 0

	return times

print(can_we_vote_dp([2, 4, 2], 4))


