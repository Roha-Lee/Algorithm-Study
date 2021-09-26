# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def _merge(curr, l1_curr, l2_curr):
            if l1_curr is None: 
                curr.next = l2_curr
                return 
            if l2_curr is None: 
                curr.next = l1_curr
                return
            if l1_curr.val < l2_curr.val:
                curr.next = l1_curr
                _merge(curr.next, l1_curr.next, l2_curr)
            else:
                curr.next = l2_curr
                _merge(curr.next, l1_curr, l2_curr.next)
                                
        result_head = ListNode(-101)
        _merge(result_head, l1, l2)
        return result_head.next
