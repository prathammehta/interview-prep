def isMoveValid(board, n, x, y):
	if x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1:
		return True
	return False

def solveKTUtil(board, current_x, current_y, pos, n):
	# print(current_x, current_y, pos)
	moves_x = [2, 1, -1, -2, -2, -1, 1, 2] 
	moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

	if pos == n**2:
		return True

	for index in range(len(moves_x)):
		new_x = current_x + moves_x[index]
		new_y = current_y + moves_y[index]

		if isMoveValid(board, n, new_x, new_y) == True:
			board[new_x][new_y] = pos
			if solveKTUtil(board, new_x, new_y, pos + 1, n) == True:
				return True

			board[new_x][new_y] = -1
	return False




def solveKT(n):

	pos = 0
	board = [[-1 for _ in range(n)] for _ in range(n)]
	board[0][0] = 0

	if solveKTUtil(board, 0, 0, 1, n) == True:
		for i in board:
			print(i)
	else:
		print('Not possible')


solveKT(8)
