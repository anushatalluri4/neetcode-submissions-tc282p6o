class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows * cols - 1
        ans = rows * cols
        while l<=r:
            mid = l+(r-l)//2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return True if ans < rows * cols and matrix[ans//cols][ans%cols]==target else False