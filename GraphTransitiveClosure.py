# https://www.geeksforgeeks.org/transitive-closure-of-a-graph-using-dfs/

from collections import defaultdict

class Graph:
	def __init__ (self, vertices):
		self.V = vertices
		self.graph = defaultdict(list)
		self.closure = [[0 for _ in range(vertices)] for _ in range(vertices)]

	def add_edge(self, source, dest):
		self.graph[source].append(dest)

	def dfs_util(self, root, vertex):
		self.closure[root][vertex] = 1
		for index in self.graph[vertex]:
			if self.closure[root][index] == 0:
				self.dfs_util(root, index)

	def find_transitive_closure(self):
		for index in range(self.V):
			self.dfs_util(index, index)

		print(self.closure)


g = Graph(4) 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
g.find_transitive_closure()