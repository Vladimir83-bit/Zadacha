try:
    number = int(input("Введите число \n"))
    if number > 0:
        print("Число больше нуля.")
    elif number == 0:
        print("Число равно нулю.")
    else:
        print("Число меньше нуля.")
except ValueError:
    print("Это не число!")