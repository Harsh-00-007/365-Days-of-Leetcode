from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Traverse the digits from right to left (least significant to most significant)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and the carry moves to the next left digit
            digits[i] = 0
            
        # If all digits were 9 (e.g., [9, 9] -> [1, 0, 0])
        return [1] + digits