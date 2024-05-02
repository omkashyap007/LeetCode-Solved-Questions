class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for i in range(len(nums)-1):
            value = nums[i]
            if value > 0 : 
                return -1
            j = i+1
            while j < len(nums):
                if nums[j] > 0 :
                    if abs(nums[j]) == abs(nums[i]) : 
                        return abs(nums[j])
                j += 1
        return -1