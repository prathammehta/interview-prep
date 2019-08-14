# https://www.geeksforgeeks.org/count-possible-paths-two-vertices/

from collections import defaultdict

class Graph:
	def __init__(self, V):
		self.graph = defaultdict(list)
		self.V = V

	def add_edge(self, source, dest):
		self.graph[source].append(dest)

	def count_paths_util(self, source, dest, visited, paths):
		visited[source] = True

		if source == dest:
			paths[0] += 1

		for item in self.graph[source]:
			if visited[item] == False:
				self.count_paths_util(item, dest, visited, paths)

		visited[source] = False

	def count_paths(self, source, dest):
		visited = [False] * self.V
		paths = [0]
		self.count_paths_util(source, dest, visited, paths)
		print(paths[0])


if __name__ == '__main__': 
  
    # Create a graph given in the  
    # above diagram  
    g = Graph(4)  
    g.add_edge(0, 1)  
    g.add_edge(0, 2)  
    g.add_edge(0, 3)  
    g.add_edge(2, 0)  
    g.add_edge(2, 1)  
    g.add_edge(1, 3)  
  
    s = 2
    d = 3
    g.count_paths(s, d)
