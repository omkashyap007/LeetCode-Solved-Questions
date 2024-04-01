class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        first_map = {}
        second_map = {}
        for i in nums1 :
            first_map[i] = first_map.get(i , 0)+1
        for i in nums2 :
            second_map[i] = second_map.get(i,0)+1
        inter = set(nums1).intersection(set(nums2))
        answer = []
        for i in inter :
            count = min(first_map[i] , second_map[i])
            for _ in range(count):
                answer.append(i)
        return answer