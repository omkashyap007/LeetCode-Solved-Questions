class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        count = l = answer = 0
        for r in range(len(nums)):
            if nums[r] == max_element : 
                count += 1
            while l <= r and count >= k :
                answer += (len(nums)-r)
                if nums[l] == max_element :
                    count -= 1
                l += 1
        return answer