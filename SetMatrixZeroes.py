class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rowIndexesToBecomeZero = set()
        colIndexesToBecomeZero = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    rowIndexesToBecomeZero.add(r)
                    colIndexesToBecomeZero.add(c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if r in rowIndexesToBecomeZero or c in colIndexesToBecomeZero:
                    matrix[r][c] = 0

