class Solution:
    def bestClosingTime(self, customers: str) -> int:
        prefix = []
        n_count = 0
        for i in customers:
            val = n_count + (i == "Y")
            prefix.append(val)
            n_count += i == "N"
        prefix.append(n_count)
        y_count = 0
        suffix = [0 for _ in range(len(customers))]
        for i in range(len(customers)-1, -1, -1):
            e = customers[i]
            val = y_count + (e == "Y")
            suffix[i] = val
            y_count += e == "Y"
        answer = float("inf")
        index = None
        for i in range(len(prefix)):
            p = prefix[i]
            s = suffix[i+1] if i+1 <= len(suffix)-1 else 0
            if p+s < answer:
                answer = p+s
                index = i
        return index
