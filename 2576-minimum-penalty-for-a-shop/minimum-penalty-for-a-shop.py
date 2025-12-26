class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n_count = 0
        y_count = 0
        suffix = [0 for _ in range(len(customers))]
        for i in range(len(customers)-1, -1, -1):
            e = customers[i]
            val = y_count + (e == "Y")
            suffix[i] = val
            y_count += e == "Y"
        answer = float("inf")
        index = None
        for i in range(len(customers)):
            e = customers[i]
            p = n_count + (e == "Y")
            n_count += e == "N"
            s = suffix[i+1] if i+1 <= len(suffix)-1 else 0
            if p+s < answer:
                answer = p+s
                index = i
        if n_count < answer:
            return len(customers)
        return index
