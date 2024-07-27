from typing import List
import operator
import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif c == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(b/a) if b/a > 0 else stack.append(math.ceil(b/a))
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(c))
        return stack.pop()
                

sol = Solution()

print(sol.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
                
                
    
