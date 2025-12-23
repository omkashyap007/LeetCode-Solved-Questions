class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        current_span = 1
        while self.stack and self.stack[-1][0] <= price:
            current_span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append((price, current_span))
        return current_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)