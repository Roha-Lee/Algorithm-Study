# without recursion 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        curr = head
        while curr.next:
            while curr.val == curr.next.val:
                curr.next = curr.next.next
                if curr.next is None: 
                    return head
                
            curr = curr.next
        return head
        
# with recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        rest = self.deleteDuplicates(head.next)
        if not head.val == rest.val:
            head.next = rest
            return head
        else:
            return rest