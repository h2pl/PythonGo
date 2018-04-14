from collections import Iterable, Iterator

list = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(list[0:3])

for key in list:
    print(key)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

[x * x for x in range(1, 11)]
[x * x for x in range(1, 11) if x % 2 == 0]




isinstance((x for x in range(10)), Iterator)


it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break