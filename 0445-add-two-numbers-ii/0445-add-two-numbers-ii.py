# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        
        # Push all digits of l1 onto stack1
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
            
        # Push all digits of l2 onto stack2
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
            
        head = None
        carry = 0
        
        # Process addition from right to left
        while stack1 or stack2 or carry:
            if stack1:
                carry += stack1.pop()
            if stack2:
                carry += stack2.pop()
                
            # Create a new node for the current digit and place it at the head
            node = ListNode(carry % 10)
            node.next = head
            head = node
            
            # Update the carry
            carry //= 10
            
        return head