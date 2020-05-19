import random
l = [777, 462, 672, 280, 939, 568, 443, 977, 944, 887, 313, 416, 780, 89, 396, 366, 330, 869, 976, 855]
print(l)

print("max is ", max(l))
print("min is ", min(l))

b = 100
for i in l:
    if b > i:
        b = i
print(b)

