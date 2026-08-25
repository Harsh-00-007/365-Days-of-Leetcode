from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0
            
            # Optimization: merge consecutive identical elements at the end
            while r > l and boxes[r] == boxes[r - 1]:
                r -= 1
                k += 1
            
            # Option 1: Remove boxes[r] along with the k attached boxes
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            
            # Option 2: Split at intermediate index i where boxes[i] == boxes[r]
            # Clear subarray (i + 1, r - 1) first to merge boxes[i] with boxes[r]
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(i + 1, r - 1, 0) + dp(l, i, k + 1))
                    
            return res

        return dp(0, len(boxes) - 1, 0)