import math

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # Edge case: Target exceeds total capacity
        if target > x + y:
            return False
        
        # Edge case: Target is 0
        if target == 0:
            return True
        
        # Check divisibility by gcd(x, y)
        return target % math.gcd(x, y) == 0