from typing import List
import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit))
        
        cache = {}
        def dfs(i):
            if i == len(intervals):
                return 0
            if i in cache:
                return cache[i]
            # don't includet
            res = dfs(i+1)
            
            # include
            j = bisect.bisect(intervals, (intervals[i][1], -1,-1))
            cache[i] = res = max(res, intervals[i][2] + dfs(j))
            return res
        
        return dfs(0)
    
sol = Solution()
print(sol.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))