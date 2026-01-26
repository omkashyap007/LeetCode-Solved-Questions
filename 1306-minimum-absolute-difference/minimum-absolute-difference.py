class Solution:
    def minimumAbsDifference(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        min_diff = float("inf")
        for i in range(1, len(nums)):
            min_diff = min(nums[i] - nums[i-1], min_diff)
        answer = []
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == min_diff:
                answer.append((nums[i-1], nums[i]))
        return answer