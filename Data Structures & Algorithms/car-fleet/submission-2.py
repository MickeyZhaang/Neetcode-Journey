class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vels = [(p, s) for p, s in zip(position, speed)]
        vels.sort()
        
        stack = []

        for i in range(len(vels) - 1, -1, -1):
            p, s = vels[i]
            time = (target - p) / s

            stack.append(time)

            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)

