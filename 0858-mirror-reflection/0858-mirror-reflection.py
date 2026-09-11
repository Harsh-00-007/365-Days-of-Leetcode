class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # Reduce p and q by dividing by 2 until one becomes odd
        while p % 2 == 0 and q % 2 == 0:
            p //= 2
            q //= 2
            
        # Determine the corner based on their final parities
        if p % 2 == 0:
            return 2
        elif q % 2 == 0:
            return 0
        else:
            return 1