class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0,1
        max_ben = 0

        while r < len(prices):
            curr_ben = prices[r] - prices[l]

            if curr_ben > 0:
                max_ben = max(max_ben, curr_ben)
            else:
                l = r
            r +=1
        return max_ben







sol = Solution()

sol_res = sol.maxProfit(prices = [1,2,4,2,5,7,2,4,9,0,9])

print(sol_res)