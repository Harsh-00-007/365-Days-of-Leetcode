class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # The 8 possible L-shaped moves for a knight
        moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        # dp[r][c] stores the probability of being at (r, c) at the current step
        dp = [[0.0] * n for _ in range(n)]
        dp[row][column] = 1.0
        
        # Iterate for each of the k steps
        for _ in range(k):
            next_dp = [[0.0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    if dp[r][c] > 0.0:
                        for dr, dc in moves:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < n and 0 <= nc < n:
                                next_dp[nr][nc] += dp[r][c] / 8.0
            dp = next_dp
            
        # Sum up all probabilities remaining on the board after k steps
        return sum(sum(row) for row in dp)