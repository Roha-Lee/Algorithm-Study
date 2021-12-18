# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head):
        dummy_head = ListNode()
        dummy_head.next = head
        curr, dummy_head.next.next = head.next, None
        while curr:
            start = dummy_head
            while start.next and start.next.val < curr.val:
                start = start.next
            start.next, curr.next, curr = curr, start.next, curr.next
        return dummy_head.next