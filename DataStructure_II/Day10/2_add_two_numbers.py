# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def zeroPadding(self, l1, l2):
        l1_len = 0
        l2_len = 0
        l1_curr = l1
        l2_curr = l2
        while l1_curr.next:
            l1_curr = l1_curr.next
            l1_len += 1
        while l2_curr.next:
            l2_curr = l2_curr.next
            l2_len += 1
        while l1_len < l2_len:
            l1_curr.next = ListNode(0)
            l1_len += 1
            l1_curr = l1_curr.next
        while l2_len < l1_len:
            l2_curr.next = ListNode(0)
            l2_len += 1
            l2_curr = l2_curr.next
        l1_curr.next = ListNode(0)
        l2_curr.next = ListNode(0)
        return l1, l2
    
    def removeLeadingZero(self, result_root):
        result = result_root.next
        prev = result
        while result.next:
            prev = result
            result = result.next 
        if result.val == 0:
            prev.next = None
        return result_root.next
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1, l2 = self.zeroPadding(l1, l2)
        l1_curr = l1
        l2_curr = l2
        result_root = ListNode(-1)
        flow = 0
        res_cur = result_root
        while l1_curr and l2_curr:
            ans = l1_curr.val + l2_curr.val + flow
            flow = 0
            if ans > 9:
                ans -= 10
                flow = 1
            res_cur.next = ListNode(ans)
            res_cur = res_cur.next
            
            l1_curr = l1_curr.next
            l2_curr = l2_curr.next
            
        return self.removeLeadingZero(result_root)
    
        
        
            