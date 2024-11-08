number = int(input("Введите число \n"))
degree = int(input("Введите степень числа \n"))
if degree >= 0 and degree < 8:
    print(number ** degree)
else:
    print("Неправильная степень.")