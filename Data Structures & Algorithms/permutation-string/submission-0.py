class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen_s1 = [0] * 26
        seen_s2 = [0] * 26

        for c in s1:
            seen_s1[ord(c) - ord('a')] += 1
        
        l = 0

        for r, c in enumerate(s2):
            # expand the window
            seen_s2[ord(c) - ord('a')] += 1

            # validity check: shrink if necesary
            if r - l + 1 > len(s1):
                seen_s2[ord(s2[l]) - ord('a')] -= 1
                l += 1

            if seen_s1 == seen_s2:
                return True
            
        return False