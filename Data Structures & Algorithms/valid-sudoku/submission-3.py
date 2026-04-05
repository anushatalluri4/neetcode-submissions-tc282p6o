class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowd = defaultdict(set)
        cold = defaultdict(set)
        square = defaultdict(set)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in rowd[i] or board[i][j] in cold[j] or board[i][j] in square[(i//3,j//3)]:
                    return False
                rowd[i].add(board[i][j])
                cold[j].add(board[i][j])
                square[(i//3,j//3)].add(board[i][j])
        return True