class Solution:

    def findProduct(self, i, j, a, b, cache):
        if i < 0 or j < 0:
            return float("-inf")
        
        if (i, j) in cache:
            return cache[(i,j)]

        take = a[i] * b[j]
        backtrack_value = self.findProduct(i-1, j-1, a, b, cache)
        take = max(take, backtrack_value, take+backtrack_value)
        
        not_take = self.findProduct(i-1, j, a, b, cache)
        not_take_both = self.findProduct(i, j-1, a, b, cache)
        max_value = max(take, not_take, not_take_both)
        cache[(i,j)] = max_value
        return max_value

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        cache = {}
        return self.findProduct(len(nums1)-1, len(nums2)-1, nums1, nums2, cache)
