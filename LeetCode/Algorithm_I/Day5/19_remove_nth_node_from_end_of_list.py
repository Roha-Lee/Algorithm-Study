# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n):
            if fast:
                fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next is None:
                break
        if fast is None: 
            return head.next
        if slow.next:
            slow.next = slow.next.next
        return head