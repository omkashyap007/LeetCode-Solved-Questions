class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = [(-score[i] , i) for i in range(len(score))]
        heapq.heapify(max_heap)
        rank = 1
        answer = [0]*len(score)
        while max_heap:
            score , index = heapq.heappop(max_heap)
            score = -score
            if rank == 0+1 :
                answer[index] = "Gold Medal"
            elif rank == 1+1 :
                answer[index] = "Silver Medal"
            elif rank == 2+1  :
                answer[index] = "Bronze Medal"
            else :
                answer[index] = str(rank)
            rank += 1
        return answer