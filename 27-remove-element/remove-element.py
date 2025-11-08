class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        if not nums:
            return 
        j = len(nums)-1
        count = 0
        while j>= 0 and nums[j] == val:
            # nums[j] = "_"
            j -= 1
            count += 1
        while i< len(nums) and j >= 0 and  i < j:
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                while j >= 0 and nums[j] == val:
                    # nums[j] = "_"
                    j -= 1
                    count += 1
            i += 1
        for _ in range(count):
            nums.pop()
