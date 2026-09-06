class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        
        for val in nums:
            curr = TreeNode(val)
            
            # All smaller elements popped were to the left of val,
            # and the largest among them becomes curr.left
            while stack and stack[-1].val < val:
                curr.left = stack.pop()
            
            # The top remaining element is greater than val and to its left,
            # so curr becomes its right child
            if stack:
                stack[-1].right = curr
                
            stack.append(curr)
            
        return stack[0]