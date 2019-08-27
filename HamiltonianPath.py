def is_safe(graph, v, path):
	if len(path) == 0:
		return True

	for item in path:
		if item == v:
			return False

	if graph[path[-1]][v] == 0:
		return False

	return True

def hamil_path_util(graph, path):
	if len(path) == len(graph):
		last_vertex = path[-1]
		first_vertex = path[0]
		if graph[first_vertex][last_vertex] == 1:
			print('FOUND', path + [first_vertex])
			return False
		else:
			return False


	for i in range(len(graph)):
		if is_safe(graph, i, path) == True:
			path.append(i)
			if hamil_path_util(graph, path) == True:
				return True
			path.pop(-1)

	return False

def hamil_path(graph):
	path = []
	if hamil_path_util(graph, path) == True:
		print(path)

graph = [[0, 1, 0, 1, 0], [1, 0, 1, 1, 1],[0, 1, 0, 0, 1,],[1, 1, 0, 0, 1],[0, 1, 1, 1, 0]]
# graph = [ [0, 1, 0, 1, 0], [1, 0, 1, 1, 1],[0, 1, 0, 0, 1,], [1, 1, 0, 0, 0],[0, 1, 1, 0, 0], ] 
hamil_path(graph)