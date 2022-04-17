def say_hello():
    a = 45
    b = 0

    if a > 5 and b < 34:
        print("a > 5")
        if a >= 45:
            print("a >= 45")
        else:
            print("a < 45")
    elif a < 5:
        print("a < 5")
    else:
        print("a == 5")

    if a == 45:
        print("a == 45")

    x = 100
    if 50 < x < 150:
        print("50 < x < 150")
    else:
        print("Something wrong.")

    return ((5 + 34) ** 2 / 53) * (24 - 6 * 3)


print(say_hello())
