class Solution:
    
    def assignBikes(self, workers, bikes):
        
        def distance(bike, worker):
            return abs(bike[0]-worker[0]) + abs(bike[1]-worker[1])
        
        def dfs(index, visited):
            if index == len(workers):
                return 0
            
            least = float('inf')
            for i in range(0, len(bikes)):
                if i not in visited:
                    new_set = visited.copy()
                    new_set.add(i)
                    least = min(least,distance(bikes[i], workers[index]) + dfs(index + 1, new_set))
                    
            return least
                
                
        
        return dfs(0, set())
        


solution = Solution()
print(solution.assignBikes([[239,904],[191,103],[260,117],[86,78],[747,62]],[[660,8],[431,772],[78,576],[894,481],[451,730],[155,28]]))
                
                        
                    