def findLongst(l1, l2):
    l = []
    maxNumber = 0
    b = 0

    for i in range(len(l1)):
        l.append([])

        for j in range(len(l2)):

            if i == 0 or j == 0:
                if l1[i] == l2[j]:
                    l[i].append(1)
                    if l[i][j] > maxNumber:
                        maxNumber = l[i][j]
                        b = j
                else:
                    l[i].append(0)

            else:
                if l1[i] == l2[j]:
                    l[i].append(l[i - 1][j - 1] + 1)
                    if l[i][j] > maxNumber:
                        maxNumber = l[i][j]
                        b = j
                else:
                    l[i].append(0)

    return l2[b - maxNumber + 1:b + 1]


def findLongst1(l1, l2):
    l = [0] * (len(l2) + 1)
    max_number = 0
    b = 0

    for i in range(len(l1)):
        for j in range(len(l2) - 1, -1, -1):
            if l1[i] == l2[j]:
                l[j + 1] = l[j] + 1
                if l[j + 1] > max_number:
                    max_number = l[j + 1]
                    b = j
            else:
                l[j + 1] = 0
    return l2[b - max_number + 1:b + 1]


if __name__ == '__main__':
    print(findLongst1(['b', 'c', 'd', 'e'], ['b', 'c']))
