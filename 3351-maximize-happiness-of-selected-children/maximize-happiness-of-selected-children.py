class Solution:
    def maximumHappinessSum(self, arr : List[int], k: int) -> int:
        arr.sort()
        dec = 0
        answer = 0
        i = len(arr)-1
        while k and i >= 0  :
            value = arr[i]-dec
            if value <= 0 :
                break
            answer += value
            dec += 1
            i -= 1
            k -= 1
        return answer 