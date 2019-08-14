def is_safe(sol, row, col):
	for i in range(col):
		if sol[row][i] == 1:
			return False

	x = row - 1
	y = col - 1
	while x >= 0 and y >= 0:
		if sol[x][y] == 1:
			return False
		x -= 1
		y -= 1

	x = row + 1
	y = col - 1
	while x < len(sol) and y >= 0:
		if sol[x][y] == 1:
			return False
		x += 1
		y -= 1

	return True		



def solve_util(sol, col):
	if col == len(sol):
		for i in sol:
			print(i)
		return True

	for row in range(len(sol)):
		if is_safe(sol, row, col) == True:
			sol[row][col] = 1
			if solve_util(sol, col + 1) == True:
				return True

		sol[row][col] = 0

	return False




def solveNQ(n):
	sol = [[0 for _ in range(n)] for _ in range(n)]
	solve_util(sol, 0)


solveNQ(4)