# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    base = 10 ** ndigits
    retVal = number * base
    decimals = retVal % 1
    if decimals <= 0.5:
        decimals = 0
    else:
        decimals = 1
    retVal //= 1
    retVal += decimals
    retVal /= base
    return retVal

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    retVal = True
    digits = []
    while (ticket_number > 0):
        digits.append(ticket_number % 10)
        ticket_number //= 10
    digitsCnt = len(digits)
    middle = digitsCnt // 2
    if digitsCnt % 2 == 0:
        retVal = sum(digits[0: middle]) == sum(digits[middle: digitsCnt])
    else:
        retVal = sum(digits[0: middle]) == sum(digits[middle + 1: digitsCnt])
    return retVal

print(lucky_ticket(123006))
print(lucky_ticket(12322))
print(lucky_ticket(436751))
