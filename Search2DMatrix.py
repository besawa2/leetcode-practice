from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bot = len(matrix)-1

        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        l, r = 0, len(matrix[row])-1
        while l <= r:
            middle = (l + r) // 2
            if target < matrix[row][middle]:
                r = middle - 1 
            elif target > matrix[row][middle]:
                l = middle + 1
            else:
                return True
        return False




        



x = Solution()
matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=24
print(x.searchMatrix(matrix,target))