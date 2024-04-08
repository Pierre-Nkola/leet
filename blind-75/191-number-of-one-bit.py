class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n % 2
            n = n >> 1

            print(count, n)
        return count
    
sol = Solution()

print(sol.hammingWeight(1011))