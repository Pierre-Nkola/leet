class Solution:
    def longestPalindrome(self, s: str) -> int:
        letter_count = {}
        count = 0
        max_odd = 0
        for c in s:
            letter_count[c] = 1 + letter_count.get(c, 0)
        for i in letter_count:
            if letter_count[i] % 2 == 0:
                count += letter_count[i]
            else:
                count += letter_count[i] - 1
    
        if count < len(s):
            count += 1
        return count + max_odd
        
        
sol = Solution()

print(sol.longestPalindrome("abccccdd"))