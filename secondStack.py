class Stackfixed:
    def __init__(self):
        self.stroge = [''] * 5
        self.index = 0

    def push(self,a):
        if self.index == 5:
            print("cannot push")
        else:
            self.stroge[self.index] = a
            self.index = self.index + 1

    def pop(self):
        if self.index == 0:
            print("cannot pop")
        else:
            self.index = self.index - 1
            return self.stroge[self.index]


q = Stackfixed()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
q.push(6)
print(q.stroge)

# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# print(q.pop())
# q.push(1)
# q.push(2)

