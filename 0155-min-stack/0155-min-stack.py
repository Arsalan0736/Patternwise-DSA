class MinStack:

    def __init__(self):
        self.stack=[]

    def push(self, value: int) -> None:
        if len(self.stack)==0:
            self.stack.append([value,value])
        else:
            curr_min=self.stack[-1][1]
            mini=min(value,curr_min)
            self.stack.append([value,mini])

    def pop(self) -> None:
        if not self.stack:
            None
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            return None
        return self.stack[-1][0]

    def getMin(self) -> int:
        if len(self.stack)==0:
            return None
        return self.stack[-1][1]
            


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()