number = int(input("Введите число от 1 до 100:\n"))
if number < 1 or number > 100:
    print("Число не в диапазоне!")
elif number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 5 == 0:
    print("Buzz")
elif number % 3 == 0:
    print("Fizz")
else:
    print(number)