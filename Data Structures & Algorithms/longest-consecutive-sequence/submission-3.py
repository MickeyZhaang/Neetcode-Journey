class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        seen = set()

        for n in nums:
            seen.add(n)

        for n in nums:

            if n-1 not in seen:
                length = 0
                while n + length in seen:
                    length += 1
                res = max(res, length)
            
        return res


            