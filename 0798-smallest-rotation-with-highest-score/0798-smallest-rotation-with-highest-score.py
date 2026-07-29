from typing import List

class Solution:
    def bestRotation(self, nums: List[int]) -> int:
        n = len(nums)
        # loss[k] tracks how many elements stop scoring a point when rotating by k
        loss = [0] * n
        
        for i, val in enumerate(nums):
            # The rotation k at which `val` becomes greater than its new index
            k_loss = (i - val + 1 + n) % n
            loss[k_loss] += 1
            
        best_k = 0
        max_score = 0
        current_score = 0
        
        # Evaluate scores for each rotation k from 0 to n - 1
        for k in range(n):
            # Each step right in k gains 1 point (from wrap-around to index n-1)
            # and loses `loss[k]` points.
            # Note: For k=0, we just accumulate the baseline relative score.
            current_score += 1 - loss[k]
            
            if current_score > max_score:
                max_score = current_score
                best_k = k
                
        return best_k