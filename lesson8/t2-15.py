number = int(input("Enter number please : "))
if 100 <= number < 1000:
    str_number = str(number)
    swapped_number = int(str_number[2] + str_number[0] + str_number[1])
    print("Ответ: перевернутое число ", swapped_number)
else:
    print("Это не 3-х значное число!")