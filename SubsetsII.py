
class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res = []
        subset = []

        def backtrack(i):
            if i > len(nums) - 1:
                res.append(tuple(subset))
                return
            
            subset.append(nums[i])
            backtrack(i+1)

            subset.pop()
            backtrack(i+1)

        backtrack(0)
        resSet = set(res)
        ans = []
        for x in resSet:
            ans.append(list(x))
        
        return ans


s = Solution()
input = [1,2,1]
print(s.subsetsWithDup(input))