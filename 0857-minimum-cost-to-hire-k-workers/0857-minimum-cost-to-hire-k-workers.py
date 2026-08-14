import heapq

class Solution:
    def mincostToHireWorkers(self, quality: list[int], wage: list[int], k: int) -> float:
        # Step 1: Pair workers with their (wage/quality ratio, quality) and sort by ratio
        workers = sorted([(w / q, q) for w, q in zip(wage, quality)])
        
        min_cost = float('inf')
        total_quality = 0
        max_heap = []  # Python's heapq is a min-heap; store negative values to simulate max-heap
        
        for ratio, q in workers:
            # Add current worker's quality to the group
            heapq.heappush(max_heap, -q)
            total_quality += q
            
            # If we exceed k workers, evict the one with the highest quality
            if len(max_heap) > k:
                highest_q = -heapq.heappop(max_heap)
                total_quality -= highest_q
                
            # When we have exactly k workers, calculate the cost
            if len(max_heap) == k:
                min_cost = min(min_cost, ratio * total_quality)
                
        return min_cost