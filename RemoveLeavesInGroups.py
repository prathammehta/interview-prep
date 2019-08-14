# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict

class Solution:
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def build_graph(self, root):
        if root.left != None:
            self.add_edge(root.val, root.left.val)
            self.build_graph(root.left)
        if root.right != None:
            self.add_edge(root.val, root.right.val)
            self.build_graph(root.right)
    
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        if root.left == None and root.right == None:
            return [[root.val]]
        
        self.graph = defaultdict(list)
        self.build_graph(root)
        
        print(self.graph)
        
        sol = []
        while len(self.graph) > 1:
            current_sol = []
            for key,value in self.graph.items():
                if key != root.val and len(value) == 1:
                    node = value.pop()
                    current_sol.append(key)
                    self.graph[node].remove(key)
                    
            for key in current_sol:
                del self.graph[key]
            
            sol.append(current_sol)
            
        sol.append([root.val])
        
        return sol
            
        
        