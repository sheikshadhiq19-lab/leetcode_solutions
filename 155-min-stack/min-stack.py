class MinStack(object):

    def __init__(self):
        self.stack=[]

    def push(self, value):
        if not self.stack:
            m = value
        else:
            m = min(value, self.stack[-1][1])
        self.stack.append((value,m))
    def pop(self):
        return self.stack.pop()
        

    def top(self):
        return self.stack[-1][0]
        

    def getMin(self):
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()