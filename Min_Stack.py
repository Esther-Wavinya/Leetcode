# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

#     MinStack() initializes the stack object.
#     void push(int val) pushes the element val onto the stack.
#     void pop() removes the element on the top of the stack.
#     int top() gets the top element of the stack.
#     int getMin() retrieves the minimum element in the stack.

# You must implement a solution with O(1) time complexity for each function.


# Example 1:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2


# Constraints:
#     -231 <= val <= 231 - 1
#     Methods pop, top and getMin operations will always be called on non-empty stacks.
#     At most 3 * 104 calls will be made to push, pop, top, and getMin.


# To implement a stack that supports push, pop, top and retrieving the minimum element in constant time, we can use two stacks.
# The first stack will store all the elements and the second stack will store the minimum elements.

class MinStack:
    # We start by initializing two stacks: stack and minStack
    def __init__(self):
        self.stack = []
        self.minStack = []
    # When we push an element val onto the stack, we first push it onto stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        # we then check if minstack is empty or if val is less than or equal to the top element of minstack. If either of these conditions is true, we push val onto minStack
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
    # When we pop an element from the stack, we first pop it from stack

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # we then check if the popped element is equal to the top element of minStack. If it is, we pop the top element of minstack
            if val == self.minStack[-1]:
                self.minStack.pop()
    # To retrieve the top element of the stack, we simply return the top element of stack

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
    # To retrieve the minimum element in the stack, we simply return the top element of minStack

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
