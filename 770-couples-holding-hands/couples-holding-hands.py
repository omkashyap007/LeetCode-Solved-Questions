class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        index_map = {}
        for i in range(len(row)):
            index_map[row[i]] = i
        count = 0
        for i in range(0 , len(row) , 2):
            a = row[i]
            b = row[i+1]
            c = a+1 if a%2 == 0 else a-1
            if b == c :
                continue
            a_index = i
            b_index = i+1
            c_index = index_map[c]
            row[b_index] , row[c_index] = row[c_index] , row[b_index]
            index_map[b] = c_index
            index_map[c] = b_index
            count +=1
        return count