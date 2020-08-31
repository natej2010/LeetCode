class Solution:
    def reverse(self, x: int) -> int:
        if x < -1:
            result = -1 * int(str(x)[:0:-1])
        else:
            result = int(str(x)[::-1])
            
        if result > 2147483647 or result < -2147483648:
            return 0
        else:
            return result
        
