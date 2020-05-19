def count(a,b):
    c = a + b
    return c

f1 = count(10,10)
f2 = count(20,20)

print(f1)
print(f2)

class stack:
    def __init__(self):
        self.storge = []

    def push(self,a):
        self.storge.append(a)

    def pop1(self):
        return self.storge.pop(-1)


q = stack
q.push(1)
q.push(2)
q.push(3)

q.pop1()
q.pop1()
q.pop1()