class UnionFind:
    """
    Class that implements the union-find structure with
    union by rank and find with path compression
    """
     
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0 for x in range(n)]
 
    def find(self, v):
        if not v == self.parent[v]:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]
 
    def union(self, x, y):
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot == yRoot:
            return
        if self.rank[xRoot] > self.rank[yRoot]:
            self.parent[yRoot] = xRoot
        else:
            self.parent[xRoot] = yRoot
            if self.rank[xRoot] == self.rank[yRoot]:
                self.rank[yRoot] += 1

        
class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        d = {}
        index = 0
        for words in pairs:
            if words[0] not in d:
                d[words[0]] = index
                index += 1
            if words[1] not in d:
                d[words[1]] = index
                index += 1
        
        uf = UnionFind(index)
        
        for words in pairs:
            uf.union(d[words[0]], d[words[1]])
        
        for word1, word2 in zip(words1, words2):
            if word1 == word2:
                continue
            
            elif uf.find(d[word1]) == uf.find(d[word2]):
                continue
            
            else:
                return False
            
        return True