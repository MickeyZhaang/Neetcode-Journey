class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]
            key = target - num
            if key in seen:
                return [seen[key], i]
            seen[num] = i
        return []
            
