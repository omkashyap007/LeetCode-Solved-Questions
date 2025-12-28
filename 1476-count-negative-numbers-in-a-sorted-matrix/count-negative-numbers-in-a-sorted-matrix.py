class Solution:

    def binarySearch(self, array):
        low, high = 0, len(array)-1
        answer = len(array)-1
        found = False
        while low <= high:
            mid = (low+high)//2
            if array[mid] < 0:
                answer = mid
                high = mid - 1
                found = True
            else:
                low = mid + 1
        if found:
            return answer
        return len(array)

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            _count = self.binarySearch(grid[i])
            print(i, _count)
            count += len(grid[0]) - _count
        return count

# [
#     [4,  3,  2, -1],
#     [3,  2,  1, -1],
#     [1,  1, -1, -2],
#     [-1,-1, -2, -3]
# ]
