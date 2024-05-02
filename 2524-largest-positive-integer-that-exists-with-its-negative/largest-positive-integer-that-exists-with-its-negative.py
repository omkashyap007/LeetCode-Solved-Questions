class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        j = len(nums)-1
        while i < j : 
            if nums[i] > 0 : 
                return -1
            if nums[j] < 0 :
                return -1
            if abs(nums[i]) == abs(nums[j]) :
                return abs(nums[i])
            elif abs(nums[i]) < abs(nums[j]) :
                j -=1 
            elif abs(nums[i]) > abs(nums[j]) :
                i += 1
                
        return -1