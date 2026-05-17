class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])*len(matrix)-1
        rows, cols = len(matrix), len(matrix[0])
        while l<=r:
            mid = (l+r)//2
            row = mid//cols
            col = mid%cols
            print(l,r)
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]<target:
                l = mid+1
            else:
                r = mid-1
        return False