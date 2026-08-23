'''
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1

        if not s:
            return 0

        longest = 1

        while r < len(s):
            while s[r] in s[l:r]:
                l += 1
            longest = max(longest, r - l + 1)
            r += 1
        return longest

                