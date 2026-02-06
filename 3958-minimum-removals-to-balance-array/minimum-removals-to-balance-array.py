class Solution:

    def binarySearch(self, i, j, k, nums):
        a = i
        answer = i
        while i<=j:
            mid = (i+j)//2
            if nums[mid] <= nums[a]*k:
                i = mid+1
                answer = mid
            else:
                j = mid-1
        return answer


    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        max_len = 0
        for i in range(len(nums)):
            j = self.binarySearch(i, len(nums)-1, k, nums)
            length = (j-i+1)
            max_len = max(length, max_len)
        return len(nums) - max_len



"""
  mid
1, 2, 6, 9


"""
