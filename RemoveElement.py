class Solution {
    public int removeElement(int[] nums, int val) {
        indexToRemove = []

        for i in range(len(nums)):
            if nums[i] == val:
                indexToRemove.append(i)
        
        popCounter = 0
        for i in range(len(sorted(indexToRemove))):
            nums.pop(indexToRemove - popCounter)
            popCounter += 1
    
        return len(nums)
    }
}