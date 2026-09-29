class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        mip = [(math.sqrt(p[0]**2 + p[1]**2), i) for i, p in enumerate(points)]
        self.mip = heapq.heapify(mip)
        
        res = []
        while len(res) < k:
            res.append(points[heapq.heappop(mip)[1]])
        return res