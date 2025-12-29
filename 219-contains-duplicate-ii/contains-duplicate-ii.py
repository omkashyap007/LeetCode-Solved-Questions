class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        hash_set = set()
        while j < len(nums):
            while (j-i) > k:
                num = nums[i]
                hash_set.remove(num)
                i += 1
            new_num = nums[j]
            if new_num in hash_set:
                return True
            hash_set.add(new_num)
            j += 1
        return False
