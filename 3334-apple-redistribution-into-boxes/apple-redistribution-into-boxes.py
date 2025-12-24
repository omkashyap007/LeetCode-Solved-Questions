class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        apple_sum = sum(apple)
        for i, c in enumerate(capacity):
            apple_sum -= c
            if apple_sum <= 0:
                return i+1
