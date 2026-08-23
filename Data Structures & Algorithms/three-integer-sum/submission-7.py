class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        sec_last = len(nums) - 1
        
        if nums[0] > 0: return []
        
        for i in range(sec_last):
            target = nums[i]
            l, r = i + 1, sec_last
            while l < r:
                the_sum = nums[l] + nums[r] + target
                if the_sum == 0:
                    addition = [nums[l], nums[r], target]
                    if addition not in result:
                        result.append(addition)
                if the_sum > 0:
                    r -= 1
                else:
                    l += 1
        return result