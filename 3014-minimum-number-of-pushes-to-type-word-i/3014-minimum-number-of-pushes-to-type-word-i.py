class Solution:
    def minimumPushes(self, word: str) -> int:
        total_pushes = 0
        
        # Iterate through each character by its index
        for i in range(len(word)):
            # Every 8 characters, the cost per press increases by 1
            total_pushes += (i // 8) + 1
            
        return total_pushes