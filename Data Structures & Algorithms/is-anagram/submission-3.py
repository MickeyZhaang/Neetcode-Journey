class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1, seen2 = [0] * 26, [0] * 26

        for i in s:
            seen1[ord(i) - ord('a')] += 1

        for i in t:
            seen2[ord(i) - ord('a')] += 1

        return seen1 == seen2

