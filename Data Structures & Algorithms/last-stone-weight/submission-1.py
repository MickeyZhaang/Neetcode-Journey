class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heaviestStones = stones
        self.heaviestStones = heapq.heapify_max(stones)

        while len(heaviestStones) > 1:
            stone1, stone2 = (
                heapq.heappop_max(heaviestStones), heapq.heappop_max(heaviestStones)
            )

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                newStone = stone2 - stone1
                heapq.heappush_max(heaviestStones, newStone)
                continue
            else:
                newStone = stone1 - stone2
                heapq.heappush_max(heaviestStones, newStone)
            
        return stones[0] if stones else 0
