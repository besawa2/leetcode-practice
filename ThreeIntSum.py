class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                l,r = i + 1, len(nums)-1
                while l < r :
                    currSum = nums[i] + nums[l] + nums[r]
                    if currSum > 0:
                        r -= 1
                    elif currSum < 0:
                        l += 1
                    else:
                        res.append([nums[i],nums[l],nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1 
                        while r > l and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1 
                        r -= 1
        return res
            
sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))