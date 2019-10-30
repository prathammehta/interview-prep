class Solution:
    def util(self, grid, m, n, i, j, length, visited):
        
        self.max_length = max(length, self.max_length)
        
        MOVES = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for move in MOVES:
            new_i = i + move[0]
            new_j = j + move[1]
            
            if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n and grid[new_i][new_j] > grid[i][j] and (new_i, new_j) not in visited:
                visited.add((new_i, new_j))
                self.util(grid, m, n, new_i, new_j, length + 1, visited)
                visited.remove((new_i, new_j))
                
                
        
        
        
    def longestIncreasingPath(self, matrix):
        
        if len(matrix) == 0:
            return 0
        
        m = len(matrix)
        n = len(matrix[0])
        
        self.max_length = 1
        MOVES = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                to_check = True
                for move in MOVES:
                    new_i = i + move[0]
                    new_j = j + move[1]
                    if new_i >= 0 and new_j >= 0 and new_i < m and new_j < n and matrix[new_i][new_j] < matrix[i][j]:
                        to_check = False
                
                if to_check:
                    print('HELLO')
                    self.util(matrix, m, n, i, j, 1, set())
                
        return self.max_length


s = Solution()
print(s.longestIncreasingPath([[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]))
        