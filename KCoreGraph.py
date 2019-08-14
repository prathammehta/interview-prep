# https://www.geeksforgeeks.org/find-k-cores-graph/

from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.graph = defaultdict(list)
        self.V = V

    def add_edge(self, start, end):
        self.graph[start].append(end)
        self.graph[end].append(start)


    def dfs_util(self, source, visited, degrees, k):
        visited[source] = 1
        
        for i in self.graph[source]:
            if degrees[source] < k:
                degrees[i] -= 1

            if visited[i] == 0:
                if self.dfs_util(i, visited, degrees, k):
                    degrees[source] -= 1

        return degrees[source] < k



    def find_k_core_graph(self,k):
        degrees = [len(adj) for vertex,adj in self.graph.items()]
        visited = [0 for _ in range(len(self.graph))]

        self.dfs_util(0,visited,degrees,k) 
  
        for i in range(self.V): 
            if visited[i] == 0: 
                self.dfs_util(i,visited,degrees,k)


        for key,value in self.graph.items():
            if degrees[key] >= k:
                print('['+str(key)+']', end='')
                for item in value:
                    if degrees[item] >= k:
                        print(' -> ' + str(item), end = '')

                print()

        # print(degrees)

g1 = Graph(9)
g1.add_edge(0, 1) 
g1.add_edge(0, 2) 
g1.add_edge(1, 2) 
g1.add_edge(1, 5) 
g1.add_edge(2, 3) 
g1.add_edge(2, 4) 
g1.add_edge(2, 5) 
g1.add_edge(2, 6) 
g1.add_edge(3, 4) 
g1.add_edge(3, 6) 
g1.add_edge(3, 7) 
g1.add_edge(4, 6) 
g1.add_edge(4, 7) 
g1.add_edge(5, 6) 
g1.add_edge(5, 8) 
g1.add_edge(6, 7) 
g1.add_edge(6, 8) 
g1.find_k_core_graph(3)
