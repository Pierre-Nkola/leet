# more efficient but a little bit more involved 


# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         l = 0
#         letter_count = {}
#         res = 0
        
#         maxf = 0
#         for r in range(len(s)):
#             letter_count[s[r]] = 1 + letter_count.get(s[r], 0)
#             maxf = max(maxf, letter_count[s[r]])
            
#             while (r-l +1 ) - maxf > k:
#                 letter_count[s[l]] -= 1
#                 l += 1
                
#             res = max(res, r-l +1)
#         return res
            
# sol = Solution()
# print(sol.characterReplacement("ABAB", k = 2))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        letter_count = {}
        res = 0
        
        for r in range(len(s)):
            letter_count[s[r]] = 1 + letter_count.get(s[r], 0)
            
            while (r-l +1 ) - max(letter_count.values) > k:
                letter_count[s[l]] -= 1
                l += 1
                
            res = max(res, r-l +1)
        return res
            
sol = Solution()
print(sol.characterReplacement("ABAB", k = 2))