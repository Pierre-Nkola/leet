class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        def pal(l, r):
            nonlocal res, resLen
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resLen = r - l + 1
                    res = s[l:r + 1]
                l -= 1
                r += 1
        
        for i in range(len(s)):
            # Odd length palindromes centered at s[i]
            pal(i, i)
            # Even length palindromes centered between s[i] and s[i+1]
            pal(i, i + 1)
        
        return res
