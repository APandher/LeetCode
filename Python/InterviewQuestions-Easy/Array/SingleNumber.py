# Solution done with no extra space and in O(nlogn)
class Solution(object):
    def singleNumber(self, nums):
        
        # could also be done using extra space with dict
        # O(nlogn)
        nums.sort()
        
        if len(nums) % 2 == 0:
            for i in range(0, len(nums), 2):
                if nums[i] != nums[i+1]:
                    return nums[i]
        else:
            for i in range(0, len(nums)-1, 2):
                if nums[i] != nums[i+1]:
                    return nums[i]
            
            return nums[-1]
