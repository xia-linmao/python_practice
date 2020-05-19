import math


def compare(a, b):
    d1 = math.ceil(math.log10(a))
    d2 = math.ceil(math.log10(b))

    d = d1 - d2

    for i in range(1, d + 2):
        f = a % (10 ** d2)
        if f == b:
            return True
        else:
            a = int(a / 10)
    return False


def contain(l):
    score = 1
    index = 0
    d = 1

    for i in range(1, len(l)):
        if l[i] > l[i - 1]:
            score += 1
        elif d < score:
            d = score
            score = 1
            index = i - 1
    if d < score:
        d = score
        index = i

    return l[index - d + 1:index + 1]


def find(l, n):
    for i in range(1, len(l) + 1):
        print(l)
        if l != None:
            if n > max(l):
                return max(l)
                break
            else:
                l.remove(max(l))
        else:
            return i









def contain2(l):

    ln = [1]

    for i in range(1, len(l)):
        l2 = l[0:i]
        minNumber = min(l2)
        minIndex = l2.index(minNumber)
        for i in range(1, len(l) + 1):
            if l2 != []:
                if l[i] > max(l2):
                    ln.append(ln[l2.index(max(l2))]+1)
                    break
                else:
                    l2.remove(max(l2))
            else:
                ln.append(ln[minIndex])

    return ln

def contain3(l):
    ln = []
    for i in range(len(l)):
        max_score = 0
        for j in range(i):
            if l[j] < l[i] and ln[j] > max_score:
                max_score = ln[j]
        ln.append(max_score+1)
    return max(ln)


if __name__ == '__main__':
    print(contain3([1,2,3,2,3]))

