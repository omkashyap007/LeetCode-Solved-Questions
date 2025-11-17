class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        index = None
        for i in range(len(nums)):
            if nums[i] == 1:
                if index is None:
                    index = i
                else:
                    print(i, index)
                    if i - index <= k:
                        return False
                    index = i
        return True