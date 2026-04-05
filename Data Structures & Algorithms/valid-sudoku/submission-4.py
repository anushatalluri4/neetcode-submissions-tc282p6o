class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowd = defaultdict(list)
        cold = defaultdict(list)
        squd = defaultdict(list)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowd[r] or board[r][c] in cold[c] or board[r][c] in squd[(r//3,c//3)]:
                    return False
                rowd[r].append(board[r][c])
                cold[c].append(board[r][c])
                squd[(r//3,c//3)].append(board[r][c])
        return True