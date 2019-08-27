
def is_empty(grid, next_point):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j] == 0:
				next_point[0] = i
				next_point[1] = j
				return True
	return False


def is_safe(grid, i, row, col):
	for j in range(len(grid)):
		if grid[row][j] == i:
			return False
		if grid[j][col] == i:
			return False

	for j in range(row - row%3, (row - row%3) + 3):
		for k in range(col - col%3, (col - col%3) + 3):
			if grid[j][k] == i:
				return False

	return True


def solve(grid):
	next_point = [0,0]
	if is_empty(grid, next_point) == False:
		return True

	row = next_point[0]
	col = next_point[1]

	for i in range(1,10):
		if is_safe(grid, i, row, col) == True:
			grid[row][col] = i
			if solve(grid) == True:
				return True
			grid[row][col] = 0

	return False



# grid=[[3,0,6,5,0,8,4,0,0], 
#       [5,2,0,0,0,0,0,0,0], 
#       [0,8,7,0,0,0,0,3,1], 
#       [0,0,3,0,1,0,0,8,0], 
#       [9,0,0,8,6,3,0,0,5], 
#       [0,5,0,0,9,0,6,0,0], 
#       [1,3,0,0,0,0,2,5,0], 
#       [0,0,0,0,0,0,0,7,4], 
#       [0,0,5,2,0,6,3,0,0]] 

grid = [
	[7,0,0,9,0,5,4,0,0],
	[0,5,0,0,0,2,0,0,6],
	[0,0,0,0,0,0,2,3,0],
	[1,8,0,6,0,0,0,0,0],
	[6,0,0,0,0,0,0,0,9],
	[0,0,0,0,0,1,0,7,3],
	[0,4,1,0,0,0,0,0,0],
	[8,0,0,1,0,0,0,2,0],
	[0,0,2,4,0,6,0,0,8]
]

if solve(grid) == True:
	for item in grid:
		print(item)
