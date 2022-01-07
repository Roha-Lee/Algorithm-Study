# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.data = ListNode()
        self.data.next = head
        self.num = 0
        
        curr = self.data.next
        while curr.next:
            self.num += 1
            curr = curr.next
        self.num += 1
        curr.next = ListNode()
    
        
    def getRandom(self) -> int:
        pos = random.randint(1, self.num)
        curr = self.data
        for _ in range(pos):
            curr = curr.next 
        return curr.val
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()