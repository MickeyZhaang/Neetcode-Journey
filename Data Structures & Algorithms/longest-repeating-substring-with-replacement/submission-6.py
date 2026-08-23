class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}

        n = len(s)

        res = 0
        max_f = 0

        l,r = 0,0

        while r < n:
            if s[r] not in seen:
                seen[s[r]] = 0
            seen[s[r]] += 1

            max_f = max(max_f, seen[s[r]])

            while r - l + 1 - max_f > k:
                seen[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        
        return res

