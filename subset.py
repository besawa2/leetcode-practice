class Solution:
# need results list, and helper array to build each subset
# using dfs helper function that takes the index of the value we're making the decision on / visiting
# if i is out of bounds (>= len(nums)), append the subset's copy and return
# to include nums[i], we append nums[i] to subset then recursively call dfs on i+1 (this is the left branch of decision tree)
# to not include nums[i], pop from subset and run dfs on i+1 again. these two calls will have different subsets provided
# and as a result give differnet answers.
# to start, pass through dfs(0) as thats the first index / value.
# return res
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums): #base case for recursion
                res.append(subset.copy()) 
                # doing a copy is like a snapshot. if we didnt use copy, it would point to variable in real time (and thats not good as subset is changing)
                return
            
            #left decision (include nums[i])
            subset.append(nums[i])
            dfs(i+1)

            #right decision (dont include nums[i])
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res
        