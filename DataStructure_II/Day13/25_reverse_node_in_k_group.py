# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        if head.next is None: return head, head
        
        curr = head
        next = temp = None
        
        while curr:
            next = curr.next
            curr.next = temp
            temp = curr
            curr = next
        return temp, head
            
        
        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        tail = head
        prev = head = None
        prev_start = prev_end = None
        start = end = None
        while True:
            for _ in range(k):
                if tail:
                    prev = tail
                    tail = tail.next
                else:
                    end.next = curr
                    return head
            
            prev.next = None 
            prev_start, prev_end = start, end
            start, end = self.reverse(curr)
            
            if head is None: 
                head = start
            else:
                prev_end.next = start
            curr = tail
            
                
        