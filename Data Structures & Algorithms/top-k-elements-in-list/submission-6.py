class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        bucket = [[] for i in range(len(nums) + 1)]
        seen = {}

        for n in nums:
            seen[n] = seen.get(n, 0) + 1

        for key, value in seen.items():
            bucket[value].append(key)
        
        for i in range(len(nums), -1, -1):
            entry = bucket[i]
            if not entry:
                continue
            for e in entry:
                res.append(e)
                if len(res) == k:
                    return res
        return res
            