class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        operations = 0
        
        # Work backward from target to startValue
        while target > startValue:
            operations += 1
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
                
        # If target <= startValue, the only option is adding 1s (startValue - target steps)
        return operations + (startValue - target)