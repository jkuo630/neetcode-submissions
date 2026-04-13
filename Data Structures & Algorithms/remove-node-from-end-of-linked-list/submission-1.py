# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # pointer
        # prev pointer

        # iterate pointer until n 
        # prev.next = pointer.next 
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # 1. Advance 'right' pointer so there is a gap of n between left and right
        while n > 0 and right:
            right = right.next
            n -= 1

        # 2. Move both until right reaches the very end (None)
        while right:
            left = left.next
            right = right.next

        # 3. 'left' is now at the node BEFORE the target. Delete the target.
        left.next = left.next.next

        return dummy.next
