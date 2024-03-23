class Solution:

    def __init__(self, w: List[int]):
        self.numbers = w
        self.length = len(w)
        prev_sum = 0
        prefix_sum = [-1 for _ in range(len(w))]
        the_sum = 0
        for i in range(len(w)):
            the_sum += w[i]
            prefix_sum[i] = the_sum
        prev_value = 0
        the_range = []
        for i in range(len(w)):
            the_range.append([prev_value ,  prefix_sum[i]])
            prev_value = prefix_sum[i] +1
        self.the_range = the_range
        self.max_value = self.the_range[-1][1]

    def binarySearch(self , number):
        high = len(self.the_range)-1
        low = 0 
        while low <= high : 
            mid = (high+low) // 2
            if self.the_range[mid][0] <= number <= self.the_range[mid][1] :
                return mid
            elif self.the_range[mid][0] < number : 
                low = mid +1
            else : 
                high = mid -1
        return -1 

    def pickIndex(self) -> int:
        random_number = random.randint(1 , self.max_value)
        return self.binarySearch(random_number)



