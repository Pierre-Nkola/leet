from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # using a counter:
        # p_count = Counter(p)
        # print( p_count)
        
        # s_count = Counter()
        # res = []
        
        # l = 0
        # for r in range(len(s)):
        #     s_count[s[r]] += 1
            
        #     if r - l + 1 > len(p):
        #         s_count[s[l]] -= 1
        #         if s_count[s[l]] == 0:
        #             del s_count[s[l]]
        #         l += 1
        #     if s_count == p_count:
        #         res.append(l)
        
        if len(p) > len(s): return []
        pCount, sCount = {},{}
        for i in range(len(p)):
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
        
        res = [0] if sCount == pCount else []
        l = 0
        
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res

                    
sol = Solution()
print(sol.findAnagrams(s = "cbaebabacd", p = "abc"))
