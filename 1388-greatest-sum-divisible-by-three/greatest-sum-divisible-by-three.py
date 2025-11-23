class Solution:

    def getMax(self, index, rem, nums, cache):
        if index >= len(nums):
            if rem %3 == 0:
                return 0
            else:
                return float("-inf")
        if (index, rem) in cache:
            return cache[(index, rem)]

        new_rem = (nums[index] + rem) % 3
        a = nums[index] + self.getMax(index+1, new_rem , nums, cache)
        b = self.getMax(index+1, rem, nums, cache)
        answer = max(a, b)
        cache[(index, rem)] = answer
        return answer

    def maxSumDivThree(self, nums: List[int]) -> int:
        cache = {}
        answer = self.getMax(0, 0, nums, cache)
        return max(answer, 0)


# index : i -> (0 : n-1)
# remainder : rem -> (0 , 1 , 2)

