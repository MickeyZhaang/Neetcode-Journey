class Solution:
    def isValid(self, s: str) -> bool:
        comp = {"]": "[", "}":"{", ")":"("}
        stack = []

        for c in s:
            if c in comp and comp[c] == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
            print(stack)
            
        
        return True if stack == [] else False