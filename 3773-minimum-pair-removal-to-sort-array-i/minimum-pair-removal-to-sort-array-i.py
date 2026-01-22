class Solution:

    def isSorted(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return True

    def findMinPair(self, nums):
        index = 0
        min_sum = float("inf")
        for i in range(len(nums)-1):
            s = nums[i] + nums[i+1]
            if s < min_sum:
                min_sum = s
                index = i
        return index, min_sum

    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0
        while not self.isSorted(nums):
            index, min_sum = self.findMinPair(nums)
            nums[index] = min_sum
            nums.pop(index+1)
            ops +=1 
        return ops
