class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        adj_list = [[] for _ in range(n)]
        for first_person , second_person , time in meetings :
            adj_list[first_person].append((second_person , time))
            adj_list[second_person].append((first_person , time))
        heap = [(0,0) , (0,firstPerson)]
        known = set()
        while heap :
            time , person = heapq.heappop(heap)
            if person in known : 
                continue
            known.add(person)
            for second_person , next_time in adj_list[person] :
                if next_time >= time :
                    heapq.heappush(heap , (next_time , second_person))
        return list(known)