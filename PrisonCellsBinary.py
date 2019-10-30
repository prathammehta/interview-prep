class Solution:
    def is_bit_set(self, n, k):
        return True if n & (1 << (k)) > 0 else False

    def get_number(self, cells):
        return int(''.join([str(i) for i in cells]),2)

    def prisonAfterNDays(self, cells, N):
        orig_state = self.get_number(cells)
        state = orig_state

        state_days_map = {}

        days = 0
        while days < N:
            temp = state
            for i in range(1,7):
                if self.is_bit_set(state, i-1) == self.is_bit_set(state, i + 1):
                    temp = temp | 1 << i
                else:
                    temp = temp & (~(1 << i))

            state = temp
            state = state & (~(1))
            state = state & (~(1<<7))
            days += 1

            
            
            if state in state_days_map:
                remaining_days = N - days
                period = days - state_days_map[state]
                skipable_days = (remaining_days // period) * period
                days += skipable_days
            else:
                state_days_map[state] = days

        result = [int(x) for x in bin(state)[2:]]
        return [0] * (8 - len(result)) + result

s = Solution()
print(s.prisonAfterNDays([1,0,0,1,0,0,1,0],1000000000))