#Author     : sakura_kyon@hotmail.com
#Question   : Min Stack
#Link       : https://oj.leetcode.com/problems/min-stack/
#Language   : python
#Status     : Accepted
#Run Time   : 548 ms
#Description: 
#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
#* 
#push(x) -- Push element x onto stack.
#* 
#pop() -- Removes the element on top of the stack.
#* 
#top() -- Get the top element.
#* 
#getMin() -- Retrieve the minimum element in the stack.
#Show Tags
#StackData Structure

#Code       : 
class MinStack:
    def __init__(self):
        self.mem = []
        self.min = []
    
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.mem.append(x)
        if self.min:
            min_add = min(self.min[-1], x)
        else:
            min_add = x
        self.min.append(min_add)

    # @return nothing
    def pop(self):
        if self.mem:
            self.min.pop()
            return self.mem.pop()
        else:
            return None

    # @return an integer
    def top(self):
        return self.mem[-1] if self.mem else None

    # @return an integer
    def getMin(self):
        return self.min[-1] if self.min else None
        