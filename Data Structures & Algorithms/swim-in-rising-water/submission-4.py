class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [(grid[0][0],0,0)]
        visit=set()
        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if r==rows-1 and c == cols-1:
                return t
            for dr, dc in directions:
                nr,nc = dr+r,dc+c
                if nr<0 or nr==rows or nc<0 or nc==cols or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap,(max(grid[nr][nc],t),nr,nc))
        
