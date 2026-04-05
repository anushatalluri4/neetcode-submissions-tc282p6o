class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowN = defaultdict(set)
        colN = defaultdict(set)
        squareN = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                if board[r][c] in rowN[r] or board[r][c] in colN[c] or board[r][c] in squareN[(r//3,c//3)]:
                    return False
                rowN[r].add(board[r][c])
                colN[c].add(board[r][c])
                squareN[(r//3,c//3)].add(board[r][c])
        return True
            