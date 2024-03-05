class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr = [(nums[i] , i) for i in range(len(nums))]
        arr.sort(key = lambda x: x[0])
        prev = float("inf")
        comps = []
        for i in range(len(arr)):
            if abs(prev-arr[i][0]) <= limit :
                comps[-1].append(arr[i])
            else :
                comps.append([arr[i]])
            prev = arr[i][0]
        for comp in comps :
            values = [i[0] for i in comp]
            indices = [i[1] for i in comp]
            indices.sort()
            i = 0
            for j in indices :
                nums[j] = values[i]
                i += 1
        return nums