import digit

# 2.1) Змінній var_int надайте значення 10, var_float -
# значення 8.4, var_str – “No”.

var_int = 10
var_float = 8.4
var_str = "No"

# 2.2) Змініть значення, збережене у змінній var_int,
# збільшивши його в 3.5 рази, результат зв'яжіть зі змінною big_int.

big_int = int(var_int * 3.5)

# 2.3) Змініть значення, збережене у змінній var_float,
# зменшивши його на одиницю, результат зв'яжіть з тією ж
# змінною.

var_float -= 1

# 2.4) Розділіть var_int на var_float, а потім big_int на
# var_float. Результат даних виразів не прив'язуйте ні до яких
# змінних

var_int / var_float
big_int / var_float

# 2.5) Змініть значення змінної var_str на
# “NoNoYesYesYes”. При формуванні нового значення
# використовуйте операції конкатенації (+) і повторення рядка (*).

var_str = "No" * 2 + "Yes" * 3

# 3. Напишіть програму digit.py, яка отримує з першого
# аргументу командного рядка ціле число, а після друкує його в
# різних системах числення

digit.thirdTask()

# 4. Виведіть значення всіх змінних. Введіть на виконання
# приклади

print(var_int)
print(var_float)
print(var_str)

# Приклад 1.1. Приклади цілих чисел
# числа в 10-овій c/ч
dec1 = 8; dec2 = -3
dec3=258028365723567
# числа в 16-овій с/ч
hex1 = 0x9; hex2 = 0xA; hex3 = 0xFF; hex4 = 0x3de
# число у двійковій с/ч
bin1 = 0b11101101
# число у 8-овій с/ч
oct1 = 0o765

# Приклад 1.2. Приклади дійсних чисел
a = 0.5; b = 3.2
# у експоненційній формі запису
c = 3.2e5 # 3.2 * 10**5
d = 1e-3 # 1 * 10**(-3)
# отримання дійсного значення
float("0.5") # з рядка
float(3) # з цілого числа

# Приклад 1.3. Приклади комплексних чисел
c1 = 2 + 3j # 2 + 3i, 2 - дійсна частина, 3 - уявна
c2 = 5 - 5j # 5 + 5i
# побудова комплексного числа з дійсного
a = 2; b = 3
c3 = complex(a, b); c4 = complex(5, -5)

# 5. Відповідно до свого варіанту отримати внутрішнє
# зображення

var1 = 459
var2 = 6578; var3 = -4596
var4 = 159.753

print(oct(var1))
print(hex(var2))
print(hex(var3))


def float_bin(number, places=3):
    whole, dec = str(number).split(".")

    whole = int(whole)
    dec = int(dec)

    res = bin(whole).lstrip("0b") + "."

    for x in range(places):
        whole, dec = str((decimal_converter(dec)) * 2).split(".")

        dec = int(dec)

        res += whole

    return res


def decimal_converter(num):
    while num > 1:
        num /= 10
    return num

print(float_bin(var4))