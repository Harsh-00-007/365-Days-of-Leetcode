# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        # 1. Find the middle (slow will point to the start of the second half)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half starting from 'slow'
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        # 3. Compare the first half and the reversed second half
        first_half, second_half = head, prev
        is_palin = True
        while second_half:
            if first_half.val != second_half.val:
                is_palin = False
                break
            first_half = first_half.next
            second_half = second_half.next
            
        # 4. (Optional) Restore the list back to original structure
        # prev_rev = None
        # curr = prev
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev_rev
        #     prev_rev = curr
        #     curr = nxt
            
        return is_palin