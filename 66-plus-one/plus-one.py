class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        i = len(digits)-1
        while digits[i] == 9:
            digits[i] = 0
            i -= 1
            carry = True
        if i == -1:
            digits.insert(0, 1)
        else:
            digits[i] += 1
        return digits
