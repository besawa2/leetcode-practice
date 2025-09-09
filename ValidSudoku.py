# Maintain collections.defaultdict(set) for each row, col, and 3x3 square. Squares are r // 3 and c // 3 as they are 3 elements wide each.
# Skip "."
# Check if c,r is in row, col, or square set. if so, return false
# If we exit loop, we know its valid

class Solution:
    def isValidSudoku(self, board):
        rows = collections.defaultdict(set)
        col = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue 
                
                if (board[r][c] in rows[r] or
                   board[r][c] in col[c] or
                   board[r][c] in squares[r//3,c//3]):
                   return False
                
                rows[r].add(board[r][c])
                col[c].add(board[r][c])
                squares[r//3, c//3].add(board[r][c])
        
        return True