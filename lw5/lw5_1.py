def triangle(x, a, b, c):
    my = 0

    if a <= x <= b:
        my = (x - a) / (b - a)
    elif b <= x <= c:
        my = (c - x) / (c - b)
    elif x <= a or c <= x:
        my = 0

    return my


i_x = int(input())
i_a = int(input())
i_b = int(input())
i_c = int(input())

if i_a < i_b < i_c:
    print(triangle(i_x, i_a, i_b, i_c))
else:
    print("Params must be: a < b < c")
