class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = nums[0]
        first_min = min(nums[1], nums[2])
        second_min = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            if nums[i] < first_min:
                first_min, second_min = nums[i], first_min
            elif nums[i] < second_min:
                second_min = nums[i]
        return answer + first_min + second_min