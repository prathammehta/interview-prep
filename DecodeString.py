class Solution:
    def process_string(self, string, r, s, e):
        stack = []
        sol = ''
        i = s
        while i < e:
            if string[i].isdigit():
                num = ''
                while string[i].isdigit():
                    num += string[i]
                    i += 1
                stack.append((i, int(num)))
            elif string[i] == ']':
                popped = stack.pop(-1) 
                start = popped[0] + 1
                repeat = popped[1]
                end = i
                string = string.replace(string[start:end+1],self.process_string(string, repeat, start, end))
            i += 1

                
        ans = ''
        i = 0
        for i in range(r):
            ans = ans + string

            
        return ans
                
        
    def decodeString(self, s: str) -> str:
        return self.process_string(s, 1, 0, len(s))
        
        

solution = Solution()
print(solution.decodeString('3[a2[c]]'))