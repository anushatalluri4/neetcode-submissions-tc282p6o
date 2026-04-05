class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        Rows, Cols = len(matrix), len(matrix[0])
        row = [False] * Rows
        col = [False] * Cols
        for i in range(Rows):
            for j in range(Cols):
                if matrix[i][j]==0:
                    row[i]=True
                    col[j]=True
        for i in range(Rows):
            for j in range(Cols):
                if row[i] or col[j]:
                    matrix[i][j]=0
        