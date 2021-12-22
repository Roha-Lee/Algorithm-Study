class Solution:
    def find_mid(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        return slow
    def reverse_list(self, curr, prev = None):
        if curr.next is None: 
            curr.next = prev
            return curr
        head = self.reverse_list(curr.next, curr)
        curr.next = prev
        return head
            
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        rev_start = self.find_mid(head)
        for_head = head
        rev_head = self.reverse_list(rev_start)
        while rev_head.next:
            for_head.next, rev_head.next, for_head, rev_head = rev_head, for_head.next, for_head.next, rev_head.next