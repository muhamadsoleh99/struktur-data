class Stack: 
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    
#membuat struktur data objek stack

s = Stack()
print(s.isEmpty())
s.push(4)
print(s.items)
s.push('dog')
print(s.items)
print(s.peek())
print(s.isEmpty())
s.push(True)
print(s.size())
s.push(8.4) 
print(s.items)
s.pop()
print(s.items)