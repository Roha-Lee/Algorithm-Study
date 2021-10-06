
# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, x):
# #         self.val = x
# #         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         history = set()
#         while headA:
#             history.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in history:
#                 return headB
#             headB = headB.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
#         history = set()
#         while headA:
#             history.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in history:
#                 return headB
#             headB = headB.next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        checkA = headA
        checkB = headB
        while checkA:
            checkA = checkA.next
            lenA += 1
        while checkB:
            checkB = checkB.next
            lenB += 1
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for _ in range(lenB - lenA):
                headB = headB.next
        while headA and headB and not headA == headB:
            headA = headA.next
            headB = headB.next    
        return headA