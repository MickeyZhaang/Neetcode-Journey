class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        checker = [0] * 26

        for i, j in zip(s, t):
            step_i = ord('a') - ord(i)
            step_j = ord('a') - ord(j)

            checker[step_i] += 1
            checker[step_j] -= 1
        
        for val in checker:
            if val != 0:
                return False

        return True