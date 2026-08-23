class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set()
        longest = 0

        for n in nums:
            seen.add(n)
        
        for n in seen:
            # start a sequence
            if n - 1 not in seen:
                start = n
                count = 0
                while start in seen:
                    count += 1
                    start += 1
                longest = max(longest, count)
        return longest