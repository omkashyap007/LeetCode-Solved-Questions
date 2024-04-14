class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        min_value = float("inf")
        while l <= r :
            mid = l + (r-l)//2
            left = nums[0]
            right = nums[len(nums)-1]
            if left <= nums[mid] >= right :
                l = mid +1
                min_value = min(min_value , nums[mid])
            elif left >= nums[mid] <= right : 
                min_value = min(min_value , nums[mid])
                r = mid-1
            else : 
                r = mid-1
                min_value = min(min_value , nums[mid])
        return min_value