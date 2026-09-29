class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.heaviestStones = stones
        heaviestStones = heapq.heapify_max(stones)
    
        print(heapq.heappop_max(heaviestStones))
        print(heapq.heappop_max(heaviestStones))
