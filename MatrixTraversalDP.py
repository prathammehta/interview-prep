# https://www.geeksforgeeks.org/min-cost-path-dp-6/

import sys

#recurse non DP
def minCost(costs, m, n):
	if m<0 or n<0:
		return sys.maxsize
	elif m == 0 and n == 0:
		return costs[m][n]
	else:
		return costs[m][n]+ min(minCost(costs,m-1,n),
								minCost(costs,m-1,n-1),
								minCost(costs,m,n-1))

def min(a,b,c):
	if a<b and a<c:
		return a
	if b<a and b<c:
		return b
	return c


# bottom up DP

def mincost_dp(costs, m, n):
	tc = [[0 for x in range(n + 1)] for x in range(m + 1)]
	tc[0][0] = costs[0][0]

	for i in range(0,m+1):
		for j in range(0,n+1):
			sol1 = sol2 = sol3 = sys.maxsize
			if i>=1:
				sol1 = tc[i-1][j]
			if j>=1:
				sol2 = tc[i][j-1]
			if j>=1 and i>=1:
				sol3 = tc[i-1][j-1]

			# print(sol1,sol2,sol3)

			if i>0 or j>0:
				tc[i][j] = min(sol1, sol2, sol3) + costs[i][j]

			# print(tc)

	return tc[m][n]

cost= [ [1, 2, 3], 
        [4, 8, 2], 
        [1, 5, 3] ] 

print(mincost_dp(cost, 2, 2))





































