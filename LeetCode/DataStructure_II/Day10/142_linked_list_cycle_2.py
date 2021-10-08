# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None: 
            return None
        
        slow = head
        fast = head
        match = False
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next
            if fast.next:
                fast = fast.next
            else:
                return None
            if slow == fast: 
                match = True
                break
            
        if match:
            slow = head
            while not slow == fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None