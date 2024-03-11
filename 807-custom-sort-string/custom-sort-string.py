class Solution:

    def mergeSort(self , arr , index_arr):
        if len(arr)>1 :
            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            self.mergeSort(left , index_arr)
            self.mergeSort(right , index_arr)
            i = j = k = 0
            while i < len(left) and j < len(right) :
                left_index = index_arr[ord(left[i]) - ord("a")]
                right_index = index_arr[ord(right[j]) - ord("a")]
                if left_index == -1 :
                    arr[k] = right[j]
                    k += 1
                    j += 1
                elif right_index == -1 : 
                    arr[k] = left[i]
                    k += 1
                    i += 1
                elif left_index <= right_index :
                    arr[k] = left[i] 
                    i += 1
                    k += 1
                else :
                    arr[k] = right[j]
                    j += 1
                    k += 1

            while i < len(left) :
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right) :
                arr[k] = right[j]
                j += 1
                k += 1
        return arr
        
    def customSortString(self, order: str, s: str) -> str:
        index_arr = [-1 for _ in range(26)]
        for index , char in enumerate(order) :
            index_arr[ord(char)-ord("a")] = index
        s = list(s)
        self.mergeSort(s , index_arr)
        return "".join(s)