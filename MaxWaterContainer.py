class Solution:
    def maxArea(self, heights) -> int:
        res = 0
        l,r = 0, len(heights)-1

        while l < r:
            area = (r-l) * min(heights[r],heights[l])
            res = max(res,area)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else: #Doesnt matter which we increment. Could make this r-=1 and save 2 lines by removing else
                l+=1
        return res
    
sol = Solution()
print(sol.maxArea(heights = [1,7,2,5,4,7,3,6]))
