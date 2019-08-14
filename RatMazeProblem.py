
def solve_maze_util(grid, path):
	current_pos = path[-1]
	if current_pos[0] == len(grid) - 1 and current_pos[1] == len(grid) - 1:
		print(path)
		return True

	moves = [[0,1],[1,0]]
	for move in moves:
		new_x = current_pos[0] + move[0]
		new_y = current_pos[1] + move[1]

		if new_x < len(grid) and new_y < len(grid) and grid[new_x][new_y] == 1:
			new_path = path.copy()
			new_path.append([new_x, new_y])
			if solve_maze_util(grid, new_path):
				return True
	return False


def solve_maze(grid):
	path = [[0,0]]
	solve_maze_util(grid, path)



solve_maze([
	[1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,1]
	])