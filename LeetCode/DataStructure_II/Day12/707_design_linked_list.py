class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)

    def get(self, index: int) -> int:
        curr = self.head
        for i in range(index + 1):
            if curr.next:
                curr = curr.next
            else:
                return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head.next
        self.head.next = new_node

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        for i in range(index):
            if curr.next:
                curr = curr.next
            else:
                return
        new_node = Node(val)
        new_node.next = curr.next
        curr.next = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for i in range(index):
            if curr.next:
                curr = curr.next
            else:
                return
        if curr.next is None:
            return
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)