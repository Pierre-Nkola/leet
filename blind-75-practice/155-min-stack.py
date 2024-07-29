class MinStack:

    def __init__(self):
        self.stack = []  # main stack to store all elements
        self.min_stack = []  # stack to store minimum values

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or the new value is less than or equal to the current minimum
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None  # Return None if the stack is empty

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        return None  # Return None if the min_stack is empty
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()