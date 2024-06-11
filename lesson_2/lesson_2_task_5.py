month = int(input("Введите число месяца (in range from 1 to 12): "))

def month_to_season(month):
        if month in [12, 1, 2]:
            print(f"Номер месяца {month} сезон Зима")
        elif month in [3, 4, 5]:
            print(f"MНомер месяца {month} сезон Весна")
        elif month in [6, 7, 8]:
             print(f"Номер месяца {month} сезон Лето")
        elif month in [9, 10, 11]:
             print(f"Номер месяца {month} сезон Осень")
        else:
             print("Вы ввели число, выходящее за пределы допустимого диапазона. Пожалуйста, попробуйте снова")
             month = int(input("Введите число месяца (in range from 1 to 12): "))
        
month_to_season(month)