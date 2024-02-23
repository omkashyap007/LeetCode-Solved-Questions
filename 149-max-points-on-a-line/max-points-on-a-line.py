class Solution:

    def gcd(self , x , y):
        if y == 0 : return x
        return self.gcd(y , x%y)

    def maxPoints(self, points: List[List[int]]) -> int:
        max_count = 1
        for i in range(len(points)):
            hash_map = {}
            for j in range(len(points)):
                if i == j :
                    continue
                first = points[i]
                second = points[j]
                dy = second[1]-first[1]
                dx = second[0]-first[0]
                value = math.atan2(dy , dx)
                hash_map[value] = hash_map.get(value,1)+1
                max_count = max(hash_map[value] , max_count)
        return max_count