num = int(input("Enter number please : "))
if 1000 <= num < 10000:
    str_num = str(num)
    swapped_num = int(str_num[3] + str_num[2] + str_num[1] + str_num[0])
    bla_bla_num = int(str_num[1] + str_num[0] + str_num[3] + str_num[2])
    bla_bla_nu2 = int(str_num[0] + str_num[2] + str_num[1] + str_num[3])
    bla_bla_nu3 = int(str_num[2] + str_num[3] + str_num[0] + str_num[1])
    # sum_num = int(str_num[0]) + int(str_num[1]) + int(str_num[2]) + int(str_num[3])
    # proiz_num = int(str_num[0]) * int(str_num[1]) * int(str_num[2]) * int(str_num[3])
    print(f"Ответ: а. - {swapped_num}, б. - {bla_bla_num}, в. - {bla_bla_nu2}, г. - {bla_bla_nu3}")
    print("Ну и костыли: ", (str_num[2]), (str_num[3]), (str_num[0]), (str_num[1]))
else:
    print("Это не 4-х значное число!")