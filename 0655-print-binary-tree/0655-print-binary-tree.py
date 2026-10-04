class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:
        # Step 1: Find the height of the tree
        def get_height(node):
            if not node:
                return -1
            return 1 + max(get_height(node.left), get_height(node.right))
        
        h = get_height(root)
        m = h + 1
        n = (1 << (h + 1)) - 1  # Equivalent to 2^(h + 1) - 1
        
        # Step 2: Initialize the matrix with empty strings
        ans = [[""] * n for _ in range(m)]
        
        # Step 3: Populate the matrix using DFS
        def dfs(node, row, left, right):
            if not node:
                return
            
            mid = (left + right) // 2
            ans[row][mid] = str(node.val)
            
            dfs(node.left, row + 1, left, mid - 1)
            dfs(node.right, row + 1, mid + 1, right)
            
        dfs(root, 0, 0, n - 1)
        
        return ans