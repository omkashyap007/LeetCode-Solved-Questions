import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        hash_map = {}
        for _, y in points:
            if y in hash_map:
                hash_map[y] += 1
            else:
                hash_map[y] = 1
        l = []
        for x in list(hash_map.values()):
            if x > 1:
                l.append((x*(x-1))//2)
        answer = 0
        MOD = 10**9+7
        l_sum_square = sum(l)**2
        sum_of_squares = sum([x*x for x in l])
        answer = (l_sum_square - sum_of_squares)//2
        return answer%MOD

# [
#     .. ,  .. ,  ..
#     .. ,  .. ,  ..
# ]

# [3, 3]

# 0 : ((1,0), (2,0), (3,0))
# 2 : ((2,2), (3,2),(4,2),(5,2),(6,2))

# top line : 2 points

# bottom line : 2 points

# 2 points that can be arranged in a way
# 3 piotns that can be arranged in a certain way

# nCr = n!/ (r!)*(n-r)!

# n*(n-1)*(n-2)...(n-r+1)
# (n-r)*(n-r-1)(n-r-2)
