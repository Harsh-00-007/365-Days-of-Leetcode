import re
from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        
        # Helper to repeatedly remove 3 or more consecutive identical balls
        def clean(s: str) -> str:
            n = -1
            while n != len(s):
                n = len(s)
                # Regex: match any character (.), followed by itself (\1) at least 2 more times
                s = re.sub(r'(.)\1{2,}', '', s)
            return s
        
        @lru_cache(None)
        def dfs(b: str, h: str) -> int:
            # Base cases
            if not b: return 0
            if not h: return float('inf')
            
            ans = float('inf')
            
            # Try placing each unique ball from our hand into the board
            for i in range(len(b) + 1):
                for c in set(h):
                    # FAANG Pruning Logic: Only insert under two conditions to avoid TLE
                    match_current = (i < len(b) and b[i] == c)
                    match_split = (0 < i < len(b) and b[i-1] == b[i] and b[i] != c)
                    
                    if match_current or match_split:
                        # Insert the ball and resolve any groupings
                        new_b = clean(b[:i] + c + b[i:])
                        
                        # Remove the used ball from hand and re-sort
                        new_h = h.replace(c, '', 1)
                        new_h = ''.join(sorted(new_h))
                        
                        # Recurse and keep the minimum
                        ans = min(ans, 1 + dfs(new_b, new_h))
                        
            return ans
        
        # Sort the hand initially so identical hands hit the same memoized cache
        hand = ''.join(sorted(hand))
        res = dfs(board, hand)
        
        return res if res != float('inf') else -1