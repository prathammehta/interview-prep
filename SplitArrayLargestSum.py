import math

class Solution:
    def splitArray(self, nums, m) -> int:
        l = r = 0
        for num in nums:
            r += num
            if l >= num:
                l = num
                
        
        ans = r
        while l <= r:
            mid = math.ceil((r+l)/2)
            seqs = 1
            current_sum = 0
            max_sum = 0
            print(' ')
            print('Mid', mid)
            for num in nums:
                if current_sum + num > mid:
                    if current_sum > max_sum:
                        max_sum = current_sum
                    seqs += 1
                    print(current_sum)
                    current_sum = num
                else:
                    current_sum += num

            print(current_sum)
            if current_sum > max_sum:
                max_sum = current_sum

            if seqs == m and max_sum < ans:
                ans = max_sum
            
            if seqs <= m:
                r = mid - 1
            else:
                l = mid + 1
                
        return ans


s = Solution()
print(s.splitArray([10,5,13,4,8,4,5,11,14,9,16,10,20,8], 8))
