# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node_dict = dict()
        curr = head
        if curr is None:
            return False
        while curr.next:
            node_dict.setdefault(curr, 0)
            if node_dict[curr]:
                return True
            node_dict[curr] = 1
            curr = curr.next
        return False