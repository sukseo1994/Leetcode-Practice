class MinStack:
    
    def __init__(self):
        self.stck = []
        self.getmin = [] 

    def push(self, val: int) -> None:
        self.stck.append(val)
        if self.getmin and self.getmin[-1][0] < val:
            self.getmin[-1][1] = self.getmin[-1][1] + 1
        else:
            self.getmin.append([val,1])
    def pop(self) -> None:
        self.stck.pop()
        self.getmin[-1][1] -= 1
        if self.getmin[-1][1] == 0:
            self.getmin.pop()

    def top(self) -> int:
        return self.stck[-1]

    def getMin(self) -> int:
        return self.getmin[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()