class MinStack:

    def __init__(self):
        self.MinStack = []  

    def push(self, val: int) -> None:
        self.MinStack.append(val)
    
    def isEmpty(self):
        return len(self.MinStack) == 0

    def pop(self) -> None:
        if self.isEmpty():
            return 'Stack is empty'
        return self.MinStack.pop()

    def top(self) -> int:
        if self.isEmpty():
            return 'Stack is empty'
        return self.MinStack[-1]

        

    def getMin(self) -> int:
        if self.isEmpty():
            return 'Stack is empty'
        return min(self.MinStack)
        
