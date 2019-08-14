# https://www.geeksforgeeks.org/water-jug-problem-using-bfs/

from collections import defaultdict

class Node:
	def __init__(self, jug1, jug2):
		self.jug1 = jug1
		self.jug2 = jug2

	def __repr__(self):
		return '(' + str(self.jug1) + ',' + str(self.jug2) + ')'

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, start_node, end_node):

		start_str = str(start_node)
		end_str = str(end_node)
		for key,value in self.graph.items():
			if start_str == str(key):
				start_node = key
			if end_str == str(key):
				end_node = key

		self.graph[start_node].append(end_node)

	def is_visited(self, node, visited):
		for item in visited:
			if str(item) == str(node):
				return True
		return False

	def print_path(self, node, pred):
		current = node
		print(node)
		while node in pred:
			print(pred[node])
			node = pred[node]

	def bfs(self, start_node, end_node, cap1, cap2):
		visited = {}
		queue = []
		queue.append(start_node)
		pred = {}
		while len(queue) > 0:
			current_node = queue.pop(0)
			visited[current_node] = True
			
			
			self.add_edge(current_node, Node(0, current_node.jug2))
			self.add_edge(current_node, Node(current_node.jug1, 0))
			self.add_edge(current_node, Node(cap1,current_node.jug2))
			self.add_edge(current_node, Node(current_node.jug1, cap2))

			amount_available_jug2 = cap2 - current_node.jug2
			if amount_available_jug2 >= current_node.jug1:
				self.add_edge(current_node, Node(0, current_node.jug2 + current_node.jug1))
			else:
				self.add_edge(current_node, Node(current_node.jug1 - amount_available_jug2, cap2))


			amount_available_jug1 = cap1 - current_node.jug1
			if amount_available_jug1 >= current_node.jug2:
				self.add_edge(current_node, Node(current_node.jug1 + current_node.jug2, 0))
			else:
				self.add_edge(current_node, Node(cap1, current_node.jug2 - amount_available_jug1))

			for child in self.graph[current_node]:
				if not self.is_visited(child, visited):
					queue.append(child)
					pred[str(child)] = str(current_node)
					if str(child) == str(end_node):
						self.print_path(str(child),pred)


g = Graph()
g.bfs(Node(0,0), Node(0, 2), 4, 3)




