class listFixed:
    def __init__(self):
        self.stroge = [''] * 6
        self.head = 0
        self.tail = 0

    def logic_add(self, i):
        return (i + 1) % 6

    def push(self, a):
        next_head = self.logic_add(self.head)
        if next_head == self.tail:
            self.pop()
        else:
            self.stroge[self.head] = a
            self.head = next_head

    def pop(self):
        if  self.head == self.tail:
            print("the list is null")
        else:
            a = self.stroge[self.tail]
            self.tail = self.logic_add(self.tail)
            return a


q = listFixed()
print(q)
q.logic_add(0)
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)

a = q.pop()
print(a)
a = q.pop()
print(a)
a = q.pop()
print(a)
a = q.pop()
print(a)
a = q.pop()
print(a)

a = q.pop()
print(a)

q.push(1)
a = q.pop()
print(a)




