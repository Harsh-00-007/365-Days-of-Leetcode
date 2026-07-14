class Solution:
    def escapeGhosts(self, ghosts: list[list[int]], target: list[int]) -> bool:
        # Calculate your Manhattan distance from the starting point (0, 0) to the target
        my_distance = abs(target[0]) + abs(target[1])
        
        # Check each ghost's Manhattan distance to the target
        for gx, gy in ghosts:
            ghost_distance = abs(gx - target[0]) + abs(gy - target[1])
            
            # If a ghost can reach the target at the same time or before you, you lose
            if ghost_distance <= my_distance:
                return False
                
        return True