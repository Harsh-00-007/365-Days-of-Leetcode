from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        # Base check: total cards must be divisible by groupSize
        if len(hand) % groupSize != 0:
            return False
        
        # Count frequency of each card
        count = Counter(hand)
        
        # Process cards starting from the smallest
        for card in sorted(count.keys()):
            if count[card] > 0:
                needed = count[card]
                
                # Check if we can form a group of size groupSize starting at 'card'
                for i in range(card, card + groupSize):
                    if count[i] < needed:
                        return False
                    count[i] -= needed
                    
        return True