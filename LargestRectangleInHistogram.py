class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index,height)

        for i, h in enumerate(heights):
            start = i #we dont know if we can extend it backwards yet
            while stack and stack[-1][1] > h: #while stack has things in it and the end of the stack's height is less than current
                index, height = stack.pop() #since our prev rectangle couldnt finish (height in i+1 was lower than i)
                maxArea = max(maxArea, height * (i - index)) #i - index is the width
                start = index #go backwards, as we know the height is bigger than current
            stack.append((start, h)) #append with new starting value, not i

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) #i is considered start value here
        
        return maxArea
        