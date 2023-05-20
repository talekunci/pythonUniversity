value = input()

while isinstance(value, str):
    try:
        value = int(value)
        break
    except:
        print("Input value must be integer. Try again:")
        value = input()


if value == 0 or value == 1:
    print(1)
    exit(0)

x = 1
result = 1
while x <= value:
    result *= x
    x += 1

print(result)
