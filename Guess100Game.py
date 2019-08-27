class Solution:
    def util(self, choices, target, my_turn):
        for choice in choices:
            if choice >= target:
                return my_turn
        
        
        win_value = False
        for i,choice in enumerate(choices):
            if self.util(choices[:i] + choices[i+1:], target - choice, not my_turn) == True:
                if my_turn:
                    return True
            else:
                if not my_turn:
                    return False

        if my_turn:
            return False
        else:
            return True
            
        
        
        
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        
        choices = [i for i in range(1, maxChoosableInteger + 1)]
        
        for i, choice in enumerate(choices):
            if choice > desiredTotal:
                return True
            
            if self.util(choices[:i] + choices[i+1:], desiredTotal - choice, False) == True:
                return True
        
        return False



s = Solution()
print(s.canIWin(15,20))