class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        i = 0 
        j = 1
        while i < len(nums) :
            if nums[i] > 0 :
                if nums[i] != j : 
                    return j
                j += 1
            i += 1
        return j

        