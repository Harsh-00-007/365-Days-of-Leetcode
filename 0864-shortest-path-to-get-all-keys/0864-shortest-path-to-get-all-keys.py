from collections import deque

class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        start_row, start_col = 0, 0
        total_keys = 0
        
        # Parse grid to find starting position and count total keys
        for r in range(m):
            for c in range(n):
                cell = grid[r][c]
                if cell == '@':
                    start_row, start_col = r, c
                elif 'a' <= cell <= 'f':
                    total_keys += 1
                    
        # All keys collected bitmask target (e.g., 3 keys -> binary 111 -> (1 << 3) - 1 = 7)
        target_keys = (1 << total_keys) - 1
        
        # Queue stores: (row, col, key_mask, steps)
        queue = deque([(start_row, start_col, 0, 0)])
        
        # Visited stores: (row, col, key_mask)
        visited = {(start_row, start_col, 0)}
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, keys, steps = queue.popleft()
            
            # Check if all keys collected
            if keys == target_keys:
                return steps
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Out of bounds or wall
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == '#':
                    continue
                
                cell = grid[nr][nc]
                new_keys = keys
                
                # Case 1: Encountered a key -> collect it (set bit)
                if 'a' <= cell <= 'f':
                    key_bit = ord(cell) - ord('a')
                    new_keys |= (1 << key_bit)
                
                # Case 2: Encountered a door -> check if we have the matching key
                elif 'A' <= cell <= 'F':
                    lock_bit = ord(cell) - ord('A')
                    if not (keys & (1 << lock_bit)):
                        continue  # Lock is closed, cannot pass
                
                # If this new state hasn't been visited, add to queue
                if (nr, nc, new_keys) not in visited:
                    visited.add((nr, nc, new_keys))
                    queue.append((nr, nc, new_keys, steps + 1))
                    
        return -1