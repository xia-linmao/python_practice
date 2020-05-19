class Stack:
    def __init__(self):
        self.storge = []


    def push(self,a):
        self.storge.append(a)

    def pop1(self):
        return self.storge.pop(-1)



q = Stack()
q.push(1)
q.push(2)
q.push(3)

print(q.pop1())
print(q.pop1())
print(q.pop1())



