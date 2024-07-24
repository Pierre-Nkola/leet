class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            raise IndexError("pop from an empty queue")
        val = self.stack[0]
        self.stack = self.stack[1:]
        return val

    def peek(self) -> int:
        if not self.stack:
            return "queue empty, try adding elements first"
        return self.stack[0]

    def empty(self) -> bool:
        return False if self.stack else True

    
sol = MyQueue()

# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()