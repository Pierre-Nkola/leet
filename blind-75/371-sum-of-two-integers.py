class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b != 0:
            temp = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = temp
        return a


sol = Solution()

print(sol.getSum(a = 5, b = 3))