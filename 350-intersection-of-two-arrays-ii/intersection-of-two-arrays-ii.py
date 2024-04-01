class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        answer = []
        for i in nums1 : 
            hash_map[i] = hash_map.get(i,0)+1
        for i in nums2 :
            if i in hash_map : 
                answer.append(i)
                hash_map[i] -= 1
                if hash_map[i]  == 0 :
                    del hash_map[i]
        return answer