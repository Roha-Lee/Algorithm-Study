# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head 
        prev = head
        while True:
            if head is None: 
                break
            if head.val == val:
                curr = prev = head = head.next
                continue
            if curr is None: 
                break
            if curr.val == val:
                prev.next = curr.next    
            else:
                prev = curr
            curr = curr.next
        return head