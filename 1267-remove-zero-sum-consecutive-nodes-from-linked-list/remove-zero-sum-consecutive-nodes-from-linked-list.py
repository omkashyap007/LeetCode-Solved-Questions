class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        thead = head
        while thead : 
            arr.append(thead.val)
            thead = thead.next
        while arr :
            for i in range(len(arr)):
                the_sum = 0
                for j in range(i , len(arr)):
                    the_sum += arr[j]
                    if the_sum == 0 :
                        start = i
                        end = j
                        new_arr = arr[:i] + arr[j+1:]
                        arr = new_arr
                        break
            if i == len(arr)-1 :
                break
        dummy = ListNode(0)
        thead = dummy
        for i in range(len(arr)):
            thead.next = ListNode(arr[i])
            thead = thead.next
        return dummy.next