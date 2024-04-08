class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r, = 0, len(nums) -1
        while l <= r:

            mid = (l+r)// 2
            print(l, r, mid)
            if nums[mid] == target:
                return mid
            # if nums[l] == target:
            #     return l
            # if nums[r] == target:
            #     return r
            
            if nums[l] <= nums[mid]: # check if left is sorted
                if target > nums[mid] or target < nums[l]:
                    l = mid +1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r] :
                    r = mid -1
                else:
                    l = mid +1
        return -1

                



        return -1

sol = Solution()

print(sol.search(nums = [4,5,6,7,0,1,2], target = 0))
