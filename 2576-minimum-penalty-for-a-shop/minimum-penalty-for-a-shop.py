class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_count = 0
        y_count = sum([i == "Y" for i in customers])
        answer = float("inf")
        index = None
        for i in range(len(customers)):
            e = customers[i]
            p = n_count + (e == "Y")            
            n_count += e == "N"
            y_count -= e == "Y"
            s = y_count
            if p+s < answer:
                answer = p+s
                index = i
        if n_count < answer:
            return len(customers)
        return index
