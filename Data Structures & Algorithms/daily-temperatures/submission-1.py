class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # hit an increase?
            while stack and temp > stack[-1][1]:
                idx, last_temp = stack.pop()
                res[idx] = i - idx
            stack.append((i, temp))
            
        return res