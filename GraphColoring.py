def is_safe(graph, v, c, color):
	for i in range(len(graph)):
		if graph[v][i] == 1 and color[i] == c:
			return False
	return True

def color_graph_util(graph, m, v, color):

	if v == len(graph):
		return True

	for i in range(1, m+1):
		if is_safe(graph, v, i, color) == True:
			color[v] = i
			if color_graph_util(graph, m, v+1, color) == True:
				return True
			color[v] = 0

	return False


def color_graph(graph, m):
	color = [0] * len(graph)
	if color_graph_util(graph, m, 0, color) == True:
		print(color)


graph = [[0,1,1,1], [1,0,1,0], [1,1,0,1], [1,0,1,0]]
color_graph(graph, 3)