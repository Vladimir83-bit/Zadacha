sec = int(input("Введите кол-во секунд: ")) 
hours = sec // 3600
minutes = (sec % 3600) // 60
seconds = sec % 60
print(f"Часы: {hours}, Минуты: {minutes}, Секунды: {seconds}")
