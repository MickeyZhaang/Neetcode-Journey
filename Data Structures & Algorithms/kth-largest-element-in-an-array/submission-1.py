class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mh = nums
        self.mh = heapq.heapify_max(mh)

        ctr = 0
        while ctr < k - 1:
            heapq.heappop_max(mh)
            ctr+=1
        return mh[0]