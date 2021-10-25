# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return 
        
        node_stack = []
        while head:
            node_stack.append(head)
            head = head.next
        
        head = node_stack.pop()
        curr = head
        while len(node_stack):
            node = node_stack.pop()
            curr.next = node
            curr = curr.next
        curr.next = None
        return head
