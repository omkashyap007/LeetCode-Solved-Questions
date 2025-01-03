class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
        suffix = [0 for _ in range(len(nums))]
        suffix[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = nums[i] + suffix[i+1]
        answer = 0
        for i in range(len(nums)-1):
            if prefix[i] >= suffix[i+1]:
                answer += 1
        return answer