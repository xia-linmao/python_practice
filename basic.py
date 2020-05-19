def math_muti():
    for i in range(1, 10):
        for j in range(1, i + 1):
            result = i * j
            print(str(i) + "*" + str(j) + "=" + str(result), end=" ")
            if i == j:
                print()


def math_add(l1, l2):
    l3 = []
    pre = 0
    l4 = []
    l5 = []

    if len(l1) >= len(l2):
        l4 = l1
        l5 = l2
    else:
        l4 = l2
        l5 = l1

    i = len(l4) - 1
    j = len(l5) - 1

    while (i >= 0):
        if j >= 0:
            k = l4[i] + l5[j] + pre
            if k <= 9:
                l3.append(k)
                pre = 0
                i = i - 1
                j = j - 1
            else:
                l3.append(k - 10)
                pre = 1
                i = i - 1
                j = j - 1
        else:
            k = l4[i] + pre
            if k <= 9:
                l3.append(k)
                pre = 0
                i = i - 1
            else:
                l3.append(k - 10)
                pre = 1
                i = i - 1
    return l3[::-1]


def math_muti1(l1, l2):
    l3 = []
    l4 = []
    l5 = []
    l6 = []
    pre = 0

    if len(l1) >= len(l2):
        l3 = l1
        l4 = l2
    else:
        l3 = l2
        l4 = l1

    for i in range(len(l4) - 1, -1, -1):
        for j in range(len(l3) - 1, -1, -1):
            if j == 0:
                k = l4[i] * l3[j] + pre

                if k <= 9:
                    l5.append(k)
                    pre = 0
                else:
                    k = (l4[i] * l3[j] + pre) % 10
                    pre = int((l4[i] * l3[j] + pre) / 10)
                    l5.append(k)
                    l5.append(pre)
                    pre = 0
            else:
                k = l4[i] * l3[j] + pre

                if k <= 9:
                    l5.append(k)
                    pre = 0
                else:
                    k = (l4[i] * l3[j] + pre) % 10
                    pre = int((l4[i] * l3[j] + pre) / 10)
                    l5.append(k)

        l6.append(l5[::-1])
        l5 = [0] * i

    return (math_add(l6[1], l6[0]))


if __name__ == '__main__':
    # math_muti()
    # print(math_add([7, 6, 9, 9, 9], [1, 1, 6]))
    # math_muti1([1, 3], [4, 2, 5])
    print(math_muti1([4, 4, 7, 3], [4, 6]))
