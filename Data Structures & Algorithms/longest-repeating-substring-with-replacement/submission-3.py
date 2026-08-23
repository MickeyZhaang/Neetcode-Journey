class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        uniques = set(s)

        n = len(s)
        res = 0

        for c in uniques:
            l,r = 0, 0
            count = 0

            while r < n:
                if s[r] == c:
                    count += 1
                while r-l+1 - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
                r += 1
        
        return res
                        

