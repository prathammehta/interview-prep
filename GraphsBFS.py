# Graphs BFS

from collections import defaultdict 

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, source, dest):
		self.graph[source].append(dest)

	def bfs(self, root):
		queue = [root]
		visited = [0] * len(self.graph)

		while len(queue) > 0:
			node = queue.pop(0)
			if visited[node] == 0:
				visited[node] = 1
				print(node, end = ' ')
				queue.extend(self.graph[node])



g = Graph()
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
g.bfs(2)
print('')



