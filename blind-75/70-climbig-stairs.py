class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        
        while n > 1:
            
            temp = two + one
            one = two
            two = temp
            
            n -=1
        return two
    
    
sol = Solution()

print(sol.climbStairs(3))