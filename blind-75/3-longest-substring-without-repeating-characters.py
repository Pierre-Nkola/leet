class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        l= 0
        res = 0
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[l])
                l += 1
            visited.add(s[i])
            res = max(res, i-l + 1)
        return res
    
sol = Solution()
print(sol.lengthOfLongestSubstring("bbbbb"))
