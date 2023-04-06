# 3. Напишіть програму digit.py, яка отримує з першого
# аргументу командного рядка ціле число, а після друкує його в
# різних системах числення

def thirdTask():
    dec = int(input())

    dBin = bin(dec)
    dOct = oct(dec)
    dHex = hex(dec)

    print(str(dec) + " " + str(dBin) + " " + str(dOct) + " " + str(dHex))
