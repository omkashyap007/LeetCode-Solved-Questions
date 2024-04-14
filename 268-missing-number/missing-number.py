class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(float("inf"))
        for i in range(len(nums)-1):
            index = abs(nums[i])
            if index == float("inf") :
                nums[0] = -nums[0]
            else : 
                value = nums[index]
                if value == 0 :
                    nums[index] = -float("inf")
                else :
                    nums[index] = -nums[index]
        for i in range(len(nums)):
            if nums[i] >= 0 :
                return i
