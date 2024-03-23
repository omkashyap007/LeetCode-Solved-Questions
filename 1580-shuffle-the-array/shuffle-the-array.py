class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr = [-1 for _ in range(len(nums))]
        i = 0
        j = n 
        for k in range(0 ,len(nums),2):
            arr[k] = nums[i]
            arr[k+1] = nums[j]
            i += 1
            j += 1
        return arr