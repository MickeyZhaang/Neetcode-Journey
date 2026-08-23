class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0] * 26

        for i in s:
            seen[ord('a') - ord(i)] += 1
        
        for i in t:
            seen[ord('a') - ord(i)] -= 1
        
        for i in seen:
            if i != 0:
                return False
        
        return True