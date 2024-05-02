class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            value = nums[i]
            if value > 0 : 
                return -1
            j = len(nums)-1
            while j > i:
                if nums[j] > 0 :
                    if abs(nums[j]) == abs(nums[i]) : 
                        return abs(nums[j])
                j -= 1
        return -1