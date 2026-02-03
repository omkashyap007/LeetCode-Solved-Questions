class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        for p in range(1, len(nums)):
            for q in range(p+1, len(nums)-1):
                l1 = nums[0:p+1] # 0-p
                l2 = nums[p:q+1] # p-q
                l3 = nums[q:len(nums)] # q - n-1
                a = True
                b = True
                c = True
                for x in range(1, len(l1)):
                    if l1[x-1] >= l1[x]:
                        a = False
                for x in range(1, len(l2)):
                    if l2[x-1] <= l2[x]:
                        b = False
                for x in range(1, len(l3)):
                    if l3[x-1] >= l3[x]:
                        c = False
                if a and b and c:
                    return True
        return False
