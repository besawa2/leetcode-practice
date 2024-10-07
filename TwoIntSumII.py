class Solution:
    def twoSum(self, numbers, target: int):#returns list of two indices indexed at 1
        l = 0
        r = len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum == target:
                return [l + 1, r + 1]
            if currSum < target:
                l +=1
            else:
                r -=1

sol = Solution()
print(sol.twoSum(numbers = [-5,-3,0,2,4,6,8], target = 5))
print(sol.twoSum(numbers = [1,2,3,5], target = 6))
