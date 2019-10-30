from collections import defaultdict
import heapq

class Graph:
	def __init__(self, edges):
		self.graph = defaultdict(list)

		for edge in edges:
			self.graph[edge[0]].append((edge[1], edge[2]))


	def shortest_path(self, source, dest):
		heap = []
		shortest_dis = {}
		visited = set()

		heap.append([source, 0, [source]])

		while len(heap):
			v1, dis, path = heapq.heappop(heap)

			visited.add(v1)

			if v1 == dest:
				return [dis, path]

			for child in self.graph[v1]:
				if child[0] not in visited:
					dis_to_child = float('inf')
					if child[0] in shortest_dis:
						dis_to_child = shortest_dis[child]

					if dis + child[1] < dis_to_child:
						shortest_dis[child] = dis + child[1]
						heapq.heappush(heap, (child[0], dis + child[1], path + [child[0]]))

		return -1




graph = Graph([
    ("A", "B", 7),
    ("A", "D", 5),
    ("B", "C", 8),
    ("B", "D", 9),
    ("B", "E", 7),
    ("C", "E", 5),
    ("D", "E", 15),
    ("D", "F", 6),
    ("E", "F", 8),
    ("E", "G", 9),
    ("F", "G", 11)
])

print(graph.shortest_path('A', 'E'))




