# Добавить 5 элементов в список и удалить первый и последний элемент (удаление сделать 2 способами - функциями и slice)
import copy

a = [a for a in range(1, 11)]
print(f"HomeWork 3.1: {a}")
# удаление 1
a.pop(0)
print(f"HomeWork 3.1: {a}")
a.pop(8)
print(f"HomeWork 3.1: {a}")
# удаление 2
a.remove(2)
print(f"HomeWork 3.1: {a}")
a.remove(9)
print(f"HomeWork 3.1: {a}")
# удаление slice
a1 = a[1:5]
print(f"HomeWork 3.1: {a1}")

# <----------------------------------------------------------------------------->
# создать список чисел от 10 до 20
x = [i for i in range(10, 21)]
print(f"HomeWork 3.2: {x}")
# <----------------------------------------------------------------------------->
# сгенерировать список [1, 1, 1, 2, 2, 2 , 3, 3, 3]
b = [1 for i in range(0, 3)]
b.extend([2, 2, 2, 3, 3, 3])
print(f"HomeWork 3.3 variant 1: {b}")
b1 = [i for i in range(1, 4)] * 3
print(f"HomeWork 3.3 variant 2: {b}")
# BeispielVariante 2
# d5 = [(i + 3) // 3 for i in range(9)]
# print(f"HomeWork 3.3 variant 3: {d5}")

# <----------------------------------------------------------------------------->
# сгенерировать список [1, 2, 1, 1, 2, 3 , 1, 2, 3]
c = [1, 2, 1]
c.extend([i for i in range(1, 4)] * 2)
print(f"HomeWork 3.4: {c}")
# <----------------------------------------------------------------------------->
# посчитать сумму чисел в списке
d = [i for i in range(1, 11)]
d = sum(d)
print(f"HomeWork 3.5: {d}")
# <----------------------------------------------------------------------------->
# создать список списков вывести список количества 2 в каждом из списков
while b.count(2):
    b.remove(2)
g = []
g.append(c)
g.append(b)
s = []
for i in g:
    if i != 0:
        s.append(c.count(2))
        s.append(b.count(2))
        break
print(f"HomeWork 3.6: {g}, список количества 2: {s}")

# <----------------------------------------------------------------------------->
# создать список списков вывести список индексов списков где нет 2
g0 = [i for i in range(1, 10, 3)]
b9 = [333, 2, 85]
n = [17, 18]
g = []
g.append(c)
g.append(b)
g.append(b9)
g.append(n)
g.append(g0)
g1 = copy.deepcopy(g)
m = []
for i in g1:
    if i.count(2):
        i.clear()
for i in g1:
    if len(i) != 0:
        m.append(g1.index(i))
print((f"HomeWork 3.7: {g}, список индексов списков где нет 2: {m}"))

# <----------------------------------------------------------------------------->
# добавить элемент в tuple
t0 = (100, 200)
elem = 300
t = copy.deepcopy(t0)
t = list(t)
t.append(elem)
t1 = tuple(t)
print((f"HomeWork 3.8: {t0} & {t1}"))

