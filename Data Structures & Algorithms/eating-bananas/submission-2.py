class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minim = float("inf")
        print(f"l: {l}, r: {r}")

        while l <= r:
            k = (r + l) // 2
            total_time = 0
            for p in piles:
                total_time += math.ceil(p / k)

            print(f"total_time: {total_time} and h: {h} and k: {k}")

            if total_time > h:
                l = k + 1
            elif total_time <= h:
                minim = min(minim, k)
                r = k - 1
        return minim