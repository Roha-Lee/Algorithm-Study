# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        next = None
        while not (curr is None or curr.next is None):
            if next is None:
                head = curr.next
            next = curr.next
            
            if curr.next.next is None:
                curr.next = curr.next.next
            else:
                if curr.next.next.next is None:
                    curr.next = curr.next.next
                else:
                    curr.next = curr.next.next.next
            temp = curr 
            curr = next.next
            next.next = temp

        return head