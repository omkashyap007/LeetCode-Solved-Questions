class Solution:
    def binaryGap(self, n: int) -> int:
        bin_n = bin(n)[2:]
        
        max_dist = 0
        last_index = 0
        
        for i in range(len(bin_n)):
            if bin_n[i] == '1':
                dist = i - last_index
                last_index = i
                
                # Replace the old record if we found a bigger gap
                if dist > max_dist:
                    max_dist = dist  
                    
        return max_dist