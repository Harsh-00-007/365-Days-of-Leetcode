# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
from typing import List

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
            
        # Step 1: Add parent pointers to all nodes
        def add_parents(node, parent):
            if node:
                node.parent = parent
                add_parents(node.left, node)
                add_parents(node.right, node)
        
        add_parents(root, None)
        
        # Step 2: BFS starting from the target node
        queue = collections.deque([(target, 0)]) # Stores tuples of (node, distance)
        seen = {target}
        
        while queue:
            # If the nodes at the front of the queue are at distance k, 
            # then all remaining nodes in the queue are at distance k.
            if queue[0][1] == k:
                return [node.val for node, dist in queue]
            
            node, dist = queue.popleft()
            
            # Explore all 3 possible directions: left child, right child, and parent
            for neighbor in (node.left, node.right, node.parent):
                if neighbor and neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, dist + 1))
                    
        return []