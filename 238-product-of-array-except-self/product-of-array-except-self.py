class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = suffix = 1
        answer = []
        for i in range(len(nums)):
            answer.append(prefix)
            prefix *= nums[i]
        for i in range(len(nums)-1 , -1 , -1):
            answer[i]*= suffix
            suffix *= nums[i]
        return answer