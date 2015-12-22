class MinStack():
    def __init__(self):
        self.items = []

    def push(self,x):
        self.items.append(x)

    def pop(self):
        self.items.pop()

    def top(self):
        return self.items[len(self.items)-1]

    def getMin(self):
        return min(self.items)

s=MinStack()
s.push(45)
s.push(5)
s.push(51)
s.push(17)
s.push(100)
s.push(1)
s.pop()

print s.items
print s.getMin()
print s.top()


