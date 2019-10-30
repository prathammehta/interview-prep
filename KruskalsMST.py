import heapq
class UnionFind:
	def __init__(self, n):
		self.size = [1] * n
		self.parents = list(range(n))

	def root(self, i):
		while self.parents[i] != i:
			self.parents[i] = self.parents[self.parents[i]]
			i = self.parents[i]
		return i

	def union(self, i, j):
		p1 = self.root(i)
		p2 = self.root(j)

		if p1 == p2:
			return

		if self.size[p1] < self.size[p2]:
			self.parents[p1] = p2
			self.size[p2] += self.size[p1]
		else:
			self.parents[p2] = p1
			self.size[p1] += self.size[p2]

	def find(self, i, j):
		return self.root(i) == self.root(j)

graph = [
	[3,0,1],
	[1,0,3],
	[3,1,3],
	[1,1,2],
	[1,3,2],
	[6,3,4],
	[5,2,4],
	[4,2,5],
	[2,4,5]
]

uf = UnionFind(6)
heap = []
for edge in graph:
	heapq.heappush(heap, edge)

sol = []
for i in range(len(graph)):
	edge = heapq.heappop(heap)
	if uf.find(edge[1], edge[2]) == False:
		sol.append((edge[1],edge[2]))
		uf.union(edge[1], edge[2])


print(sol)











