number = int(input("Enter number please : "))
if 1000 <= number < 10000:
    str_number = str(number)
    sum_number = int(str_number[0]) + int(str_number[1]) + int(str_number[2]) + int(str_number[3])
    proiz_number = int(str_number[0]) * int(str_number[1]) * int(str_number[2]) * int(str_number[3])
    print(f"Ответ: Сумма - {sum_number}, произведение - {proiz_number}")
else:
    print("Это не 4-х значное число!")