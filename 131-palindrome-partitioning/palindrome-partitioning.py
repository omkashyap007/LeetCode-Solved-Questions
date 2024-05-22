class Solution:

    def getPalindromes(self , index , array , string , answer):
        if index >= len(string) :
            answer.append(list(array))
            return
        for i in range(index , len(string)):
            t = string[index:i+1]
            if t==t[::-1] : 
                array.append(t)
                self.getPalindromes(i+1 , array , string , answer)
                array.pop()  

    def partition(self, s: str) -> List[List[str]]:
        answer = []
        self.getPalindromes(0 , [] , s , answer)
        return answer