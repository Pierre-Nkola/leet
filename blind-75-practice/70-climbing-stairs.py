# Not optimal solution
# class Solution:
#     def climbStairs(self, n: int):
#         def fib(n):
#             if n <= 3:
#                 return n
#             else:
#                 return fib(n-1) + fib(n-2)
            
#         return fib(n)

# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 2:
#             return n
        
#         dp = [0] * (n+1)
#         dp[1] = 1
#         dp[2] = 2
        
#         for i in range(3, n+1):
#             dp[i] = dp[i-1] + dp[i-2]
            
#         print(dp)
#         return dp[n]
    
class Solution:
    def climbStairs(self, n: int):
        if n <= 2:
            return n
        a,b = 1,2
        
        for i in range(3,n+1):
            a,b = b, b + a
        return b
sol = Solution()

print(sol.climbStairs(5))