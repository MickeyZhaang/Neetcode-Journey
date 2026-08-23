class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        seen = {}
        l = 0

        maxf = 0
        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            maxf = max(maxf, seen[s[r]])

            while (r - l + 1) - maxf > k:
                seen[s[l]] -= 1
                l+=1
            longest = max(longest, r - l + 1)

        return longest