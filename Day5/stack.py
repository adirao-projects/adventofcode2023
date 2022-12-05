class Stack:
    def __init__(self, size: int) -> None:
        self.size = size
        self.stack = [None]*size
        
    def push(self, value) -> None:
        i=0
        while self.stack[i]==None:
            if i == self.size-1:
                return False
            else:
                i=i+1    
        self.stack[i] = value
        return True
        
    def pop(self):
        i = self.size-1
        while self.stack[i]==None:
            if i == 0:
                return False
            else:
                i=i-1
        value = self.stack[i]
        self.stack[i]=None
        
        return value