# https://www.spoj.com/problems/PPATH/
from collections import defaultdict

def is_transformable(num1, num2): #To compare the digits s1 = str(num1) s2 = str(num2) c = 0
	s1 = str(num1) 
	s2 = str(num2) 
	c = 0
	if (s1[0] != s2[0]): c += 1
	if (s1[1] != s2[1]): c += 1
	if (s1[2] != s2[2]): c += 1
	if (s1[3] != s2[3]): c += 1
	return c == 1

class Graph:
	def __init__ (self):
		self.graph = defaultdict(list)

	def add_edge(self, source, dest):
		self.graph[source].append(dest)
		self.graph[dest].append(source)

	def build_adj_list(self, primes):
		for number1 in primes:
			for number2 in primes:
				if is_transformable(number1, number2):
					self.add_edge(number1, number2)

	def bfs(self, start, end):
		if start == end:
			return 0
		
		queue = []
		visited = {}
		queue.append(start)
		visited[start] = 0

		
		while len(queue):
			current = queue.pop(0)
			for child in self.graph[current]:
				if not child in visited:
					visited[child] = visited[current] + 1
					queue.append(child)
					if child == end:
						return visited[child]

		return -1








def get_array_with_primes(n):
	is_prime = [True for _ in range(n+1)]
	p = 2
	while p*p <= n:
		if is_prime[p] == True:
			for i in range(p*p, n+1, p):
				is_prime[i] = False
		p += 1

	primes = []

	for index in range(2,n+1):
		if is_prime[index] == True and index >= 1000:
			primes.append(index)

	return primes


primes = get_array_with_primes(9999)
g = Graph()
g.build_adj_list(primes)
print(g.bfs(1033, 1033))


