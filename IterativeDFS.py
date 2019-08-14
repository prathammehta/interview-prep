# https://www.geeksforgeeks.org/iterative-depth-first-traversal/

from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def add_edge(self, source, dest):
		self.graph[source].append(dest)

	def dfs(self, source):
		stack = []
		visited = [0] * self.V
		stack.append(source)
		while len(stack) > 0:
			current = stack.pop(-1)
			visited[current] = 1
			print(current)
			for item in self.graph[current]:
				if visited[item] == 0:
					stack.append(item)


g = Graph(5); # Total 5 vertices in graph  
g.add_edge(1, 0);  
g.add_edge(0, 2);  
g.add_edge(2, 1);  
g.add_edge(0, 3);  
g.add_edge(1, 4);  
  
print("Following is Depth First Traversal")  
g.dfs(0) 
