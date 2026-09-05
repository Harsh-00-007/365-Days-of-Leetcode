class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        sum_a = sum(aliceSizes)
        sum_b = sum(bobSizes)
        
        # The required difference bob's candy must have over alice's candy
        delta = (sum_b - sum_a) // 2
        
        # Store Bob's sizes in a set for O(1) average lookup
        bob_set = set(bobSizes)
        
        for x in aliceSizes:
            target_y = x + delta
            if target_y in bob_set:
                return [x, target_y]