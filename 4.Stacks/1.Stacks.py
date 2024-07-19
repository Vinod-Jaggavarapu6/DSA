from typing import List 

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        if len(self.stack) == 0:
            return None
        return self.stack.pop()
    def is_empty(self):
        return len(self.stack) == 0
    def size(self):
        return len(self.stack)
    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[-1]
    def sum(self):
        sum = 0
        for ele in self.stack:
            sum+=ele
        return sum

# LC-682 : Baseball Game

def calPoints(operations: List[str]) -> int:
        # Intuition: We use stack to keep track of the scores and operations. We iterate through the operations and perform the respective operations.
        # TimeComplexity: O(n)
        # SpaceComplexity: O(n)

        stack = Stack()
        
        for operation in operations:
            print(stack.stack)
            if operation == '+':
                score1 = stack.pop()
                score2 = stack.pop()
                sum = score1+score2
                stack.push(score2)
                stack.push(score1)
                stack.push(sum)

            elif operation == 'D':
                score = stack.peek()*2
                stack.push(score)

            elif operation == 'C':
                stack.pop()
            else:
                stack.push(int(operation))
        
        return stack.sum()

# LC-20 : Valid Parentheses

def isValid(s: str) -> bool:
        stack = []

        map = {
                '(':')',
                '{':'}',
                '[':']'
            }
        
        for c in s:
            if c in map:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if map[stack.pop()] != c:
                    return False
        
        return len(stack) == 0


#LC-155 : Min Stack
class MinStack:
    # Intuition: We use two stacks one for keeping track of the elements and the other for keeping track of the minimum element at that point.

    # TimeComplexity: O(1)
    # SpaceComplexity: O(n)

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def push(self,val):
        self.stack.append(val)

        if self.min_stack:
           min_val = min(self.min_stack[-1],val)
           self.min_stack.append(min_val)
        else:
            self.min_stack.append(val)
        

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]
    

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# print(minStack.getMin())
# minStack.pop()
# print(minStack.top())
# print(minStack.getMin())


# print(isValid("()"))
# print(isValid("()[]{}"))
# print(isValid("]"))

# calPoints(["5","2","C","D","+"])