class Solution:

    def binarySearch(self, array):
        low, high = 0, len(array)-1
        answer = len(array)
        while low <= high:
            mid = (low+high)//2
            if array[mid] < 0:
                answer = mid
                high = mid - 1
            else:
                low = mid + 1
        return answer

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            count += len(grid[0]) - self.binarySearch(grid[i])
        return count
