# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        v = head
        vv = head 
        while vv.next:
            if not vv.next is None:
                v = v.next
                vv = vv.next
                if not vv.next is None:
                    vv = vv.next
            
        return v