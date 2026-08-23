class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minim = float('inf')

        while l <= r:
            mid = (r + l) // 2
            cur = nums[mid]
            print(cur)

            if cur > nums[r]:
                l = mid + 1
            elif cur <= nums[r]:
                minim = min(minim, nums[mid])
                r = mid -1 
        
        return minim