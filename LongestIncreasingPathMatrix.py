# https://www.geeksforgeeks.org/longest-increasing-path-matrix/

def return_longest_increasing_path_matrix(mat, m, n):
	max_seq_length = [[0 for _ in range(0, n)] for _ in range(0, m)]
	max_seq_prev = [[-1 for _ in range(0, n)] for _ in range(0, m)]
	max_seq_length[0][0] = mat[0][0]
	max_seq_prev[0][0] = 1
	
	for i in range(1,m):
		if mat[i][0] > mat[i-1][0] and max_seq_prev[i-1][0] >= 1:
			max_seq_length[i][0] = max_seq_length[i-1][0] + 1
			max_seq_prev[i][0] = 1
			max
		pass

	for j in range(1,n):
		if mat[0][j] > mat[0][j-1] and max_seq_prev[0][j-1] >= 1:
			max_seq_length[0][j] = max_seq_length[0][j-1] + 1
			max_seq_prev[0][j] = 2
		pass

	largest_value = 0
	largest_i = 0
	largest_j = 0

	for i in range(1,m):
		for j in range(1,n):
			value1 = 0
			value2 = 0
			if mat[i][j] > mat[i-1][j] and max_seq_prev[i-1][j] >= 1:
				value1 = max_seq_length[i-1][j]
			if mat[i][j] > mat[i][j-1] and max_seq_prev[i][j-1] >= 1:
				value2 = max_seq_length[i][j-1]
			if value1 > value2:
				max_seq_length[i][j] = value1 + 1
				max_seq_prev[i][j] = 1
			elif value2 > 0:
				max_seq_length[i][j] = value2 + 1
				max_seq_prev[i][j] = 2


	return max_seq_length

print(return_longest_increasing_path_matrix([
	[1, 2, 3, 4],
	[2, 2, 3, 4],
	[3, 2, 3, 4],
	[4, 5, 6, 7]
	],4,4))


 # 1 2 3 4
 # 2 0 0 0
 # 3 0 0 0
 # 4 5 6 7
