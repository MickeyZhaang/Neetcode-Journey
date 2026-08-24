class Solution:
    def isValid(self, s: str) -> bool:
        comp = {"]": "[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c in comp:
                stack.pop()
            else:
                stack.append(c)
        
        return True if not stack else False