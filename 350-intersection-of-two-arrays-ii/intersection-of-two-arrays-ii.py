class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i = j = 0 
        answer = []
        while i < len(nums1) and j < len(nums2) :
            first = nums1[i]
            second = nums2[j]

            if first == second : 
                answer.append(nums1[i])
                i += 1
                j += 1
            elif first > second :
                j += 1
            else : 
                i += 1
        return answer