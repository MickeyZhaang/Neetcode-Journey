class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        most = 0

        while l < r:
            lower = min(heights[l], heights[r])
            water = lower * (r - l)
            most = max(water, most)
            if (heights[l] < heights[r]):
                l += 1
            else:
                r -= 1
        
        return most