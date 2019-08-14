# https://www.geeksforgeeks.org/path-rectangle-containing-circles/

from collections import defaultdict
import math

def get_node_string(row,col):
	return str(row) + '-' + str(col)

def get_distance(x1, y1, x2, y2):
	distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
	# print(x1, y1, x2, y2, distance)
	return distance

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def print_path(self, node, pred):
		path = []
		while node in pred:
			path.insert(0, node)
			node = pred[node]

		path.insert(0, node)
		print(path)


	def add_edge(self, row1, col1, row2, col2):
		self.graph[get_node_string(row1, col1)].append(get_node_string(row2, col2))
		self.graph[get_node_string(row2, col2)].append(get_node_string(row1, col1))

	def bfs(self, m, n, k, r, X, Y):
		blocked = set()
		for i in range(1,m+1):
			for j in range(1,n+1):
				for circle_index in range(k):
					if get_distance(i,j,X[circle_index], Y[circle_index]) <= float(r):
						blocked.add(get_node_string(i,j))

		if get_node_string(1,1) in blocked:
			return -1

		visited = {}
		pred = {}
		start = get_node_string(1,1)
		queue = []
		queue.append(start)
		visited[start] = True

		while len(queue) > 0:
			current = queue.pop(0)
			visited[current] = True
			i,j = current.split('-')
			i = int(i)
			j = int(j)

			if i == m and j == n:
				self.print_path(get_node_string(i,j),pred)
				return

			if j<n and get_node_string(i, j+1) not in blocked:
				self.add_edge(i,j,i,j+1)
			if i<m and get_node_string(i+1, j) not in blocked:
				self.add_edge(i,j,i+1,j)
			if i>1 and get_node_string(i-1, j) not in blocked:
				self.add_edge(i,j,i-1,j)
			if j>1 and get_node_string(i, j-1) not in blocked:
				self.add_edge(i,j,i,j-1)

			for child in self.graph[current]:
				if child not in visited:
					pred[child] = current
					queue.append(child)

		return -1




g = Graph()
g.bfs(5,5,2,1,[1,3],[3,3])

