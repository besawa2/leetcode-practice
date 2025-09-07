class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, cur, total): #keeping track of current index i, current helper list (empty at start), and running total
            if total == target:
                res.append(cur.copy()) #if we find a match, append a copy of it to res
                return
            if i >= len(nums) or total > target: #if we go out of bounds for nums, or if the running total exceeds our target:
                return #that means we have no use here, we can just end this recursive path


            #two decisions here: include nums[i] and go down left path, or dont include nums[i] and go down right path
            #left decision: include nums[i] in the future / now
            cur.append(nums[i])
            backtrack(i, cur, total + nums[i])

            #right decision; dont include nums[i] ever again
            cur.pop() #cleaning up cur, as we had to append it above for left decision
            backtrack(i+1, cur, total) #i+1 to move forward in the nums list and take the previous num out of consideraiton

        #initialized starting at 0th index, with cur being empty, and total being 0
        backtrack(0, [], 0)
        return res
        