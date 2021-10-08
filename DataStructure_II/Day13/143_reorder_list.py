# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        deq = deque()
        curr = head.next
        while curr:
            deq.append(curr)
            curr = curr.next 
        
        toggle = False
        curr = head
        while len(deq):
            toggle = not toggle
            if toggle: 
                node = deq.pop()
            else:
                node = deq.popleft()
            node.next = None
            curr.next = node
            curr = curr.next
        return head
        
    