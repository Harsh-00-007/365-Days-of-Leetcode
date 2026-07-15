class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        n = len(start)
        
        # Pointers for start (i) and end (j) strings
        i, j = 0, 0
        
        while i < n or j < n:
            # Advance pointer i to the next non-'X' character
            while i < n and start[i] == 'X':
                i += 1
                
            # Advance pointer j to the next non-'X' character
            while j < n and end[j] == 'X':
                j += 1
                
            # If one string is exhausted, the other must also be exhausted
            if i == n or j == n:
                return i == j
            
            # The non-'X' characters must be the exact same
            if start[i] != end[j]:
                return False
            
            # 'L' can only move left: its starting index must be >= ending index
            if start[i] == 'L' and i < j:
                return False
                
            # 'R' can only move right: its starting index must be <= ending index
            if start[i] == 'R' and i > j:
                return False
            
            # Move to the next characters
            i += 1
            j += 1
            
        return True