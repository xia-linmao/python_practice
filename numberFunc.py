def sort1(num_list):
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if num_list[i] > num_list[j]:
                tmp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = tmp
    return num_list


# def sort2(lst):
#     for j in range(1, len(lst)):
#         for i in range(len(lst) - j):
#             if lst[i] < lst[i + 1]:
#                 a = lst[i]
#                 lst[i] = lst[i + 1]
#                 lst[i + 1] = a
#
#     return lst
#
#
# def sort3(l):
#     for i in range(1, len(l)):
#         current = l[i]
#
#         for j in range(i, -1, -1):
#             if l[j - 1] > current:
#                 l[j] = l[j - 1]
#             else:
#                 break
#
#         l[j] = current
#
#     return l
#
#
# def sort4(l):
#     for i in range(1, len(l)):
#         curent = l[i]
#         for j in range(i - 1, -1, -1):
#             if curent > l[j]:
#                 break
#             else:
#                 l[j + 1] = l[j]
#                 l[j] = curent
#     return l


def sort5(l):
    for j in range(0, len(l) - 1):
        current = l[j]
        place = j
        for i in range(j, len(l)):
            if l[i] < current:
                current = l[i]
                place = i
        l[place] = l[j]
        l[j] = current

    return l

def found(l1,l2):
    a = -1
    for i in range(len(l1)-len(l2)+1):
        l3 = l1[i:i+len(l2)]
        if l3 == l2:
            a = i
    if a == -1:
        return "No"
    else:
        return "Yes"

def compare(n1,n2):
    n = n1.count(n2)
    print(n)
    if n == 0:
        print("no")
    else:
        print("yes")





if __name__ == '__main__':
    # print(found([4,5,6,6,7,4,2,1,2,3,4,2,1],[2,3,10]))
    compare("123","45")
