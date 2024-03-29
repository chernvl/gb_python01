# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

print("Задача 1: ")

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
xPos = equation.find('x')
k = float(equation[equation[0: xPos].rfind(' ') + 1: xPos])
b = float(equation[equation.rfind(' ') + 1: len(equation)])
res = 0
if equation.find('+') != -1:
    res = k * x + b
else:
    res = k * x - b
print(res)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
#date = '01.11.1985'

# Примеры некорректных дат
#date = '01.22.1001'
#date = '1.12.1001'
#date = '-2.10.3001'

print("Задача 2:")
date = input("Введите дату: ")
longMonths = {1, 3, 5, 7, 8, 10, 12}
dayPoint = date.find('.')
monthPoint = date.rfind('.')
res = "Correct"
if dayPoint != 2 or monthPoint - dayPoint - 1 != 2 or len(date) - monthPoint - 1 != 4:
    res = "Incorrect"
else:
    day = int(date[0: dayPoint])
    month = int(date[dayPoint + 1: monthPoint])
    year = int(date[monthPoint + 1: len(date)])
    if month < 1 or month > 12 or year < 1 or year > 9999 or day < 1:
        res = 'Incorrect'
    elif month in longMonths and day > 31:
        res = 'Incorrect'
    elif day > 30:
        res = 'Incorrect'
print(res)

# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3