class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        minHeap = [[grid[0][0],0,0]] 
        visit = set()
        N = len(grid)
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        visit.add((0,0))
        while minHeap:
            time, r, c = heapq.heappop(minHeap)
            if r == N-1 and c == N-1:
                return time
            for dr, dc in directions:
                nr, nc =  dr+r, dc+c
                if nr not in range(N) or nc not in range(N) or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap, [max(time,grid[nr][nc]),nr,nc])
            

        