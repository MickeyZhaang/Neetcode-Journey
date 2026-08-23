class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        longest = 0
        result = 0
        
        for i in range(len(s)):
            if s[i] in map:
                longest = max(map[s[i]] + 1, longest)
            map[s[i]] = i
            result = max(result, i - longest + 1)
        return result
