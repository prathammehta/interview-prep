import math
class Solution:
    def maximizeSweetness(self, sweetness, K):

        sol = 0
        
        l = min(sweetness)
        r = sum(sweetness)
        
        k = K + 1

        
        while l <= r:
            m = math.ceil((l+r)/2)
            pieces = 0
            total = 0
            for s in sweetness:
                total += s
                if total >= m:
                    total = 0
                    pieces += 1
                    
            if pieces < k:
                r = m - 1
            elif pieces > k:
                l = m + 1
            else:
                sol = max(sol, m)
                l = m + 1
                
        return sol


s = Solution()
print(s.maximizeSweetness([1,2,2,1,2,2,1,2,2], 2))