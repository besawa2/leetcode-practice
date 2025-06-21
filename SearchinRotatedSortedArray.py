from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        if len(nums) == 1 and nums[0] == target:
            return 0
        while l <= r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m -1
                else:
                    l = m + 1 
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

                
        

x = Solution()
nums=[1,5]
target=5
print(x.search(nums,target))