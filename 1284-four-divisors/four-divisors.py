class Solution:

    def findDivisorsSum(self, num):
        _count = 0
        _sum = 0
        for i in range(1, int(num**(0.5)) + 1):
            if num%i == 0:
                if i == num//i:
                    _count += 1
                else:
                    _count += 2
                    _sum += i
                _sum += num//i
                if _count > 4:
                    return None
        if _count == 4:
            return _sum
        return None

    def sumFourDivisors(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            div_sum = self.findDivisorsSum(num)
            if div_sum is not None:
                answer += div_sum
        return answer
