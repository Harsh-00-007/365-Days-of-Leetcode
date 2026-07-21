import random
import bisect
from typing import List

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_sums = []
        
        # Calculate the cumulative number of points
        current_total = 0
        for x1, y1, x2, y2 in rects:
            # Number of integer points in the current rectangle
            points_in_rect = (x2 - x1 + 1) * (y2 - y1 + 1)
            current_total += points_in_rect
            self.prefix_sums.append(current_total)

    def pick(self) -> List[int]:
        # 1. Pick a random target point out of the total available points
        total_points = self.prefix_sums[-1]
        target = random.randint(1, total_points)
        
        # 2. Find which rectangle this target point belongs to using binary search
        rect_idx = bisect.bisect_left(self.prefix_sums, target)
        
        # 3. Retrieve the boundaries of the chosen rectangle
        x1, y1, x2, y2 = self.rects[rect_idx]
        
        # 4. Pick a random x and random y within those boundaries
        return [random.randint(x1, x2), random.randint(y1, y2)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()