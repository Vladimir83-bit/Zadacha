number = int(input("Enter number please : "))
if 100 <= number < 1000:
    str_number = str(number)
    swapped_number = int(str_number[2] + str_number[1] + str_number[0])
    sum_number = int(str_number[0]) + int(str_number[1]) + int(str_number[2])
    print(f"Ответ: перевернутое число {swapped_number}, его сумма {sum_number}")
else:
    print("Это не 3-х значное число!")