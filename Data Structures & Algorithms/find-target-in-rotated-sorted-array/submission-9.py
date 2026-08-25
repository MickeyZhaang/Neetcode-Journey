class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            
            # when we found it...
            if target == nums[m]:
                return m
            
            # right sorted
            if nums[m] <= nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                    
            # left sorted
            elif nums[m] > nums[r]:
                if target <= nums[r] < nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1


            
