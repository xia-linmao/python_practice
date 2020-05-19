class Shui:
    def __init__(self):
        self.storge = []
    def shuixianhua(self):
        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    a = i * 100 + j * 10 + k
                    b = i * i * i + j * j * j + k * k * k
                    if a == b:
                        self.storge.append(a)
        return self.storge

q = Shui()
print(q.shuixianhua())