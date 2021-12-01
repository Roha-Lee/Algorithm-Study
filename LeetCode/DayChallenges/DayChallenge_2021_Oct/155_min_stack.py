class MinStack:
    
    def __init__(self):
        self.data = []    
        self.min_data = (float("Inf"), -1)
        
    def push(self, val: int) -> None:
        self.data.append((val, self.min_data[1]))
        if self.min_data[0] > val:
            self.min_data = (val, len(self.data)-1)

    def pop(self) -> None:
        val, idx = self.data.pop()
        if val == self.min_data[0]:
            if idx == -1:
                new_min = float("Inf")
            else:
                new_min, _ = self.data[idx]
            self.min_data = (new_min, idx)
        
    
    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        return self.min_data[0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()