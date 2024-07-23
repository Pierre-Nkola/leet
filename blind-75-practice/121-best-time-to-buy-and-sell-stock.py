from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0,1
        res = 0
        
        while r < len(prices):
            cur_diff = prices[r] - prices[l]
            
            if cur_diff > 0:
                res = max(res, cur_diff)
            else:
                l = r
            r += 1
        return res
    
sol = Solution()
print(sol.maxProfit(prices = [7,1,5,3,6,4]))
            
                
