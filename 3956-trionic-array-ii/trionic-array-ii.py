class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        ans = a = b = c = -float("inf")
        prev = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            na = nb = nc = -float("inf")

            # Increasing
            if curr > prev:
                na = max(a, prev) + curr
                nc = max(b, c) + curr

            # Decreasing
            elif curr < prev:
                nb = max(a, b) + curr

            a, b, c = na, nb, nc
            ans = max(ans, c)
            prev = curr

        return ans