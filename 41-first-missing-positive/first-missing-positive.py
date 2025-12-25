class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: clean up invalid values
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        # Step 2: mark presence
        for i in range(n):
            x = abs(nums[i])
            if 1 <= x <= n:
                if nums[x - 1] > 0:
                    nums[x - 1] = -nums[x - 1]

        # Step 3: find first missing
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1
