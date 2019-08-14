import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        map = {}
        for c in S:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1
                
        heap = []
        for key, value in map.items():
            heap.append(value)
            
        heapq._heapify_max(heap)
        
        first = heapq._heappop_max(heap)
        second = heapq._heappop_max(heap)
        while second > 0:
            first =- 1
            second =- 1
            heap.append(first)
            heap.append(second)
            heapq._heapify_max(heap)
            first = heapq._heappop_max(heap)
            second = heapq._heappop_max(heap)
            
        if first > 1:
            return False
        
        return True
            
sol = Solution()
print(sol.reorganizeString('aab'))