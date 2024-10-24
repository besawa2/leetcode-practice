class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums)-1
        found = False
        while not found:
            newList = []
            middle = len(nums)//2 
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[middle] == target:
                return middle
            if nums[middle] > target:
                if middle >= 1:
                    for i in range(l, middle):
                        newList.append(nums[i])
                        r = len(newList) - 1
                    nums = newList

            elif nums[middle] < target:
                if middle <= len(nums)-1:
                    for i in range(middle, r+1):
                        newList.append(nums[i])
                        left = middle+1
                        r = len(newList) - 1
                    nums = newList
            if len(newList) == 2:
                return -1
                
    
sol = Solution()
print(sol.search(nums=[-1,0,3,5,9,12]
,target=9))