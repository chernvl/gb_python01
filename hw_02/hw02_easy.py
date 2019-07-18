# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("Задание 1:")
fruits = ["яблоко", "банан", "киви", "арбуз", "виноград"]
maxLen = 0
for fruit in fruits:
    if len(fruit) > maxLen:
        maxLen = len(fruit)

i = 0
while i < len(fruits):
    text = f"{i}. {fruits[i]:>{maxLen}}"
    print(text)
    i += 1


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("\nЗадание 2:")
import random
l1 = []
l2 = []
for i in range(0, 100):
    l1.append(random.randint(-100, 100))
    l2.append(random.randint(-100, 100))
print("List 1:", l1)
print("List 2:", l2)
idx = 0
while idx < len(l1):
    foundInSecond = False
    for l in l2:
        if l == l1[idx]:
            foundInSecond = True
    if foundInSecond:
        l1.pop(idx)
    else:
        idx += 1
print("Resulted List:", l1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("\nЗадание 3:")
import random
l1 = []
for i in range(0, 100):
    l1.append(random.randint(-100, 100))
print("List 1:", l1)
idx = 0
while idx < len(l1):
    if l1[idx] % 2 == 0:
        l1[idx] = l1[idx] * 1.0 / 4
    else:
        l1[idx] *= 2
    idx += 1
print("Resulted List:", l1)