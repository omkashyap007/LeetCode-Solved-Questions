class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.size = 4 * n
        self.sum = [0] * self.size
        self.mn  = [0] * self.size
        self.mx  = [0] * self.size

    def _pull(self, node: int):
        l, r = node * 2, node * 2 + 1
        self.sum[node] = self.sum[l] + self.sum[r]
        self.mn[node] = min(self.mn[l], self.sum[l] + self.mn[r])
        self.mx[node] = max(self.mx[l], self.sum[l] + self.mx[r])

    def update(self, idx: int, val: int):
        node, l, r = 1, 0, self.n - 1
        path = []
        while l != r:
            path.append(node)
            m = l + (r - l) // 2
            if idx <= m:
                node = node * 2
                r = m
            else:
                node = node * 2 + 1
                l = m + 1
        self.sum[node] = val
        self.mn[node] = val
        self.mx[node] = val
        while path:
            self._pull(path.pop())

    def find_rightmost_prefix(self, target: int) -> int:
        node, l, r, sum_before = 1, 0, self.n - 1, 0
        if not (self.mn[node] <= target - sum_before <= self.mx[node]):
            return -1
        while l != r:
            m = l + (r - l) // 2
            lchild, rchild = node * 2, node * 2 + 1
            sum_before_right = self.sum[lchild] + sum_before
            need_right = target - sum_before_right
            if self.mn[rchild] <= need_right <= self.mx[rchild]:
                node = rchild
                l = m + 1
                sum_before = sum_before_right
            else:
                node = lchild
                r = m
        return l


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        stree = SegmentTree(n)
        first = {}
        result = 0

        for l in range(n - 1, -1, -1):
            num = nums[l]
            old = first.get(num)
            if old is not None:
                stree.update(old, 0)
            first[num] = l
            stree.update(l, 1 if num % 2 == 0 else -1)
            r = stree.find_rightmost_prefix(0)
            if r >= l:
                result = max(result, r - l + 1)

        return result