from typing import List
from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping the characters count with the list of anagrams
        
        for s in strs:
            count = [0] * 26 # a-z
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)
        return res.values()
            
sol = Solution()

print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
