import bisect
from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0
        
        for house in houses:
            # Find the index of the first heater >= house
            idx = bisect.bisect_left(heaters, house)
            
            # Distance to the closest heater on the right
            right_dist = heaters[idx] - house if idx < len(heaters) else float('inf')
            # Distance to the closest heater on the left
            left_dist = house - heaters[idx - 1] if idx > 0 else float('inf')
            
            # Minimum distance for the current house
            min_dist = min(left_dist, right_dist)
            # The global radius must cover all houses, so take the maximum of minimums
            max_radius = max(max_radius, min_dist)
            
        return max_radius