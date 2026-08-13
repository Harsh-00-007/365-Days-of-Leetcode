class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = {tuple(obs) for obs in obstacles}
        
        # Directions ordered clockwise: North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        x, y = 0, 0
        dir_idx = 0  # Starts facing North
        max_dist_sq = 0
        
        for cmd in commands:
            if cmd == -1:
                # Turn right 90 degrees
                dir_idx = (dir_idx + 1) % 4
            elif cmd == -2:
                # Turn left 90 degrees
                dir_idx = (dir_idx + 3) % 4
            else:
                # Move forward cmd steps
                dx, dy = directions[dir_idx]
                for _ in range(cmd):
                    next_x, next_y = x + dx, y + dy
                    
                    # Stop if an obstacle blocks the way
                    if (next_x, next_y) in obstacle_set:
                        break
                    
                    x, y = next_x, next_y
                    max_dist_sq = max(max_dist_sq, x * x + y * y)
                    
        return max_dist_sq