import heapq
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        edges = [
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
        ]
        for edge in edges:
            self.add_edge(*edge)

    def add_edge(self, i, j, cost):
        self.graph[i].append((j,cost))


    def shortest_path(self, source, target):
        heap = []
        seen = set()
        mins = {}
        heap.append((0, source, []))

        while len(heap) > 0:
            cost, v1, path = heapq.heappop(heap)
            if v1 not in seen:
                
                if v1 == target:
                    return cost, path+[v1]
                
                seen.add(v1)
                
                for v2, step_cost in self.graph[v1]:
                    if v2 not in seen:
                        min_d_v2 = None
                        if v2 in mins:
                            min_d_v2 = mins[v2]

                        if min_d_v2 == None or min_d_v2 > cost + step_cost:
                            mins[v2] = cost + step_cost
                            heapq.heappush(heap,(cost + step_cost, v2, path + [v1]))

        return 'Not possible'







g = Graph()
print(g.shortest_path('A', 'E'))


