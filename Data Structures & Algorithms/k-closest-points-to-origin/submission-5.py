class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x : x[0]**2 + x[1]**2
        def partition(l,r):
            pivot = r
            pivotdist = euclidean(points[pivot])
            i = l
            for j in range(l,r):
                if euclidean(points[j])<pivotdist:
                    points[i],points[j] = points[j],points[i]
                    i+=1
            points[i], points[r] = points[r], points[i]
            return i
        pivot = len(points)
        l, r = 0, len(points)-1
        while pivot!=k:
            pivot = partition(l,r)
            if pivot < k:
                l = pivot + 1
            else:
                r = pivot - 1
        return points[:k]
