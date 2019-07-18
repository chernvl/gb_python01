# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    fib = [1, 1]
    for idx in range(2, m):
        fib.append(fib[idx - 1] + fib[idx - 2])
    return fib[n - 1:m - 1]

print(fibonacci(7, 10))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

def sort_to_max(origin_list):
    for i in range(0, len(origin_list)):
        for j in range(0, i):
            if origin_list[i] < origin_list[j]:
                k = origin_list[i]
                origin_list[i] = origin_list[j]
                origin_list[j] = k
    return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(func, my_list):
    retVal = []
    for elem in my_list:
        if func(elem):
            retVal.append(elem)
    return retVal

l1 = [1, 17, -2, 3, 13, 4, 23]
print(my_filter(lambda x : x > 10, l1))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

def isParallelogram(A1, A2, A3, A4):
    retVal = False

    return retVal

A1 = (1, 3)
A2 = (4, 7)
A3 = (2, 8)
A4 = (-1, 4)
print(isParallelogram(A1, A2, A3, A4))