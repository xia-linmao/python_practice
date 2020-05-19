class Fei:
    def __init__(self):
        self.stroge = [1, 1]

    def fei(self, j):
        if j == 0 or j == 1:
            return 1
        else:
            for i in range(2, j+1):
                self.stroge.append(self.stroge[i - 1] + self.stroge[i - 2])
        return self.stroge[j]

        # if j == 0 or j == 1:
        #     return 1
        # else:
        #     for i in range(0, j - 2):
        #         self.stroge.append(self.stroge[i] + self.stroge[i + 1])
        #     return self.stroge[-1]



q = Fei()
print(q.fei(5))




