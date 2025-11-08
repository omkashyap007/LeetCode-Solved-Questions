class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, item in enumerate(nums):
            k = target-item
            if k in hash_map:
                return [hash_map[k], i]
            hash_map[item] = i
        return [-1, -1]
