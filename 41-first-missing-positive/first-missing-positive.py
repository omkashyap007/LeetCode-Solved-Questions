class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hasOne = False
        for index, num in enumerate(nums):
            if num == 1:
                hasOne = True
            if num <= 0 or num > len(nums):
                nums[index] = 1
        if not hasOne:
            return 1

        for index in range(len(nums)):
            num = abs(nums[index])
            idx = num-1
            if nums[idx] < 0: continue
            nums[idx] = -1 * nums[idx]

        for i in range(len(nums)):
            if nums[i] > 0:
                return i+1
        return len(nums)+1        

            
