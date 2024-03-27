class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        answer = left = 0
        for right in range(len(nums)):
            product *= nums[right]
            while left <= right and product >= k : 
                product//=nums[left]
                left += 1
            answer += (right-left+1)
        return answer