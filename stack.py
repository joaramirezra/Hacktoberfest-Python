class Stack:
    def __init__(self, size):
        self.TOP = -1
        self.size = size
        self.structure = []

    def check_empty(self):
        if self.TOP == -1:
            return True
        return False
    
    def check_full(self):
        if self.TOP == self.size-1:
            return True
        return False
    
    def push(self, val):
        if self.check_full():
            return "Stack is filled already"
        self.TOP += 1
        self.structure.insert(self.TOP, val)
    
    def pop(self):
        if self.check_empty():
            return "stack is empty"
        deleted = self.structure.pop(self.TOP)
        self.TOP -= 1
        return deleted


stack1 = Stack(5)
result = []
for i in "Boy":
    print(stack1.push(i))
for i in range(3):
    result.append(stack1.pop())
print("".join(result))
