class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if(len(t) > len(s)):
            return ""
    
        minim = float("inf")
        res = []
        seen_s, seen_t = {}, {}
        seen_t = {t[i]: seen_t.get(t[i],0) + 1 for i in range(len(t))}

        l = 0
        have = 0
        need = len(seen_t)

        for r, c in enumerate(s):
            if c not in seen_t:
                continue
            seen_s[c] = seen_s.get(c, 0) + 1
            if seen_s[c] == seen_t[c]:
                have += 1
            while have == need:
                if s[l] in seen_s: 
                    seen_s[s[l]] -= 1
                    if seen_s[s[l]] < seen_t[s[l]]:
                        have -= 1
                    cur_min = minim
                    minim = min(minim, r - l + 1)
                    if cur_min != minim:
                        res = [l, r]
                l += 1
        return s[res[0]:res[1]+1] if res else ""
                