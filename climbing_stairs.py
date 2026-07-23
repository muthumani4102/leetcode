class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

    
        prev = 3
        
        prev_prev = 2
        current = 0

        for _ in range(3, n):
            current = prev + prev_prev
            prev_prev = prev
            prev = current
        
        return current