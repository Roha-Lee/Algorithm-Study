class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, x):
        self.stack1.append(x)
    
    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q.dequeue())
q.enqueue(6)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())