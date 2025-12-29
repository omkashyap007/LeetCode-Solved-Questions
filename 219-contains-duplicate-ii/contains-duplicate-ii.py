class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        hash_map = {}
        while j < len(nums):
            while (j-i) > k:
                num = nums[i]
                hash_map[num] -= 1
                if hash_map[num] == 0:
                    del hash_map[num]
                i += 1
            new_num = nums[j]
            if new_num in hash_map:
                return True
            hash_map[new_num] = 1
            j += 1
        return False
