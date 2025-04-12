def sum():
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть введіть останнє число: "))

    if a > b:
        a, b = b, a

    s = 0
    for i in range(a, b + 1):
        s += i

    return s


r = sum()
print(f"Сума діапазону дорівнює {r}")
