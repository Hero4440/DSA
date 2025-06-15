# https://leetcode.com/problems/min-stack/
# 155. Min Stack
# Medium
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, val: int) -> None:
        self.append(val)
        minVal = min(val , self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
    def pop(self) -> int:
        self.minStack.pop()
        return self.stack.pop()
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]
# Time Complexity: O(1) Space Complexity: O(n)



        
    