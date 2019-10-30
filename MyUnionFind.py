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


u = UnionFind(10)
u.union(1,9)
u.union(2,8)
print(u.find(1,9))
print(u.find(1,2))
u.union(9,8)
print(u.find(1,2))