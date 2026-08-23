class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        freq_map = [[] for i in range(len(nums))]
        res = []

        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1
        
        for key, v in counter.items():
            freq_map[v - 1].append(key)
        
        top_k = 1

        for i in range(len(nums) - 1, -1, -1):
            if freq_map[i]:
                idx = 0
                while top_k <= k and idx < len(freq_map[i]):
                    res.append(freq_map[i][idx])
                    idx += 1
                    top_k += 1
        return res
                