# https://www.geeksforgeeks.org/longest-arithmetic-progression-dp-35/

def longest_ap(arr,n):
	mat = [[0 for _ in range(n)] for _ in range(n)]

	for i in range(n):
		mat[i][n-1] = 2

	for j in range(n-2,0,-1):
		i = j-1
		k = j+1
		while(i >= 0 and k < n):
			if 2*arr[j] < arr[i] + arr[k]:
				k += 1
			elif 2*arr[j] < arr[i] + arr[k]:
				mat[i][j] = 2
				i -= 1
			else:
				mat[i][j] = mat[j][k] + 1
				i -= 1
				k += 1

		while i>=0:
			mat[i][j] = 1
			i -= 1


	return mat


a = [5, 10, 15, 20, 25, 30]
for x in longest_ap(a, len(a)):
	print(x)


