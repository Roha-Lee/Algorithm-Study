# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: return head
        if head.next is None: return head
        same = False
        prev = None
        cur = head 
        while cur.next:
            if cur.val == cur.next.val:
                cur = cur.next
                same = True
            else: 
                if same:
                    if prev is None:
                        head = cur.next
                    else:
                        prev.next = cur.next
                    cur = cur.next
                    same = False                        
                else:
                    prev = cur
                    cur = cur.next

        if same: 
            if prev is None:
                head = cur.next
            else:
                prev.next = cur.next
            cur = cur.next
            same = False 
        else:
            prev = cur
            cur = cur.next
        return head
