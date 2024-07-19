class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()]).lower()
        l, r = 0, len(s) -1
        
        if s == "":
            return True
        
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        
        return True
        

sol = Solution()

print(sol.isPalindrome(s = "aa"))