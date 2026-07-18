# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a placeholder dummy node to easily return the head of the new list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Keep looping as long as there are nodes to add OR a leftover carry
        while l1 or l2 or carry:
            # Get the current values; if a list is finished, default its value to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum for the current place value
            total = val1 + val2 + carry
            
            # Update the carry for the next column calculation
            carry = total // 10
            
            # Create the new node with the single digit value
            current.next = ListNode(total % 10)
            
            # Move the output list pointer forward
            current = current.next
            
            # Move input pointers forward if they haven't reached the end
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy.next