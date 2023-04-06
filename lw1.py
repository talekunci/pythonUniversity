import math
import random

# 1) У кожному рядку визначити тип і значення змінної

a = 5       # type integer
n = input()  # пользователь вводит цифру 8 - type string
c = int(n)  # type integer
d = a * c   # type integer
d = d - a   # type integer
s = "Рамамбахарумамбуру"  # type string
d = n + str(a)  # type string
m = n + s       # type string

# 2) Вивести на екран три введених з клавіатури числа в
# порядку, зворотному їх введення

a = int(input())
b = int(input())
c = int(input())

print(c)
print(b)
print(a)

# 3) Ввести з клавіатури два числа і вивести цілу частину від
# ділення першого на друге.

a = int(input())
b = int(input())

print(a // b)

# 4) Ввести з клавіатури основа і висоту трикутника і вивести
# площу трикутника

b = int(input())
h = int(input())

print(1/2 * b * h)

# 5) Ввести з клавіатури два катета трикутника і вивести
# гипотенузу

c1 = int(input())
c2 = int(input())
h = (c1 ** 2) + (c2 ** 2)

print(math.sqrt(h))

# 6) Згенерувати випадкове двозначне число, вивести на екран
# це число, а також суму і добуток його цифр.

a = random.randint(10, 100)
print(a)
print((a // 10) + (a % 10))
print((a // 10) * (a % 10))

# 7) Ввести основи і висоту трапеції і вивести площу трапеції.

a = int(input())
b = int(input())
h = int(input())
print(((a + b) / 2) * h)

# 8) Отримати випадкове тризначне число, вивести це число і
# суму його окремих цифр.

r = str(random.randint(100, 1000))

print(r)
print(int(r[0]) + int(r[1]) + int(r[2]))
print(int(r[0]) * int(r[1]) * int(r[2]))

# 9) Програма, яка розраховує вік людини в годинах.

age = int(input())
ageInHours = age * 365 * 24

print(ageInHours)
