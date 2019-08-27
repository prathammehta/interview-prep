class Solution:
    def util(self, prices, index, holding):
        if index >= len(prices):
            return 0
        
        if holding:
            return max(
                self.util(prices, index + 1, True),
                prices[index] + self.util(prices, index + 2, False)
            )
        
        return max(
            self.util(prices, index+1, False),
            self.util(prices, index+1, True) - prices[index]
        )
        
    def maxProfit(self, prices):
        
        return self.util(prices, 0, False)
        

s = Solution()
print(s.maxProfit([1,2,3,0,2]))