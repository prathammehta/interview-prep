# Graphs DFS

from collections import defaultdict 

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, source, dest):
		self.graph[source].append(dest)

	def dfs(self, source, visited):
		if visited[source] == 1:
			return
		else:
			print(source, end=' ')
			visited[source] = 1
			for node in self.graph[source]:
				self.dfs(node, visited)

g = Graph()
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
g.dfs(2,[0] * 4)
print('')
