ver = "v2.8.0"
# обработка исключений get_integer_input
# дефолтные значения параметров
# # # # # # # # # # # # # # # # #
# TODO
# # # # # # # # # # # # # # # # #
# примера \ примеров - добавить проверку на русский язык
# добавить оценку по прохождению теста
# добавить вычитание \ сложение с выбором
# объединить строку ввода информации в одну строку (or  \ and)
# # # # # # # # # # # # # # # # #


# всякие импорты
import random
import datetime

# дефолтные значения параметров
# сложение
MIN_OPERAND_ADDITION = 1
MAX_OPERAND_ADDITION = 99
# вычитание  
MIN_OPERAND_SUBTRACTION = 1
MAX_OPERAND_SUBTRACTION = 99
# умножение 
MIN_OPERAND_MULTIPLICATION = 2
MAX_OPERAND_MULTIPLICATION = 9
# деление 
MIN_OPERAND_DIVISION = 2
MAX_OPERAND_DIVISION = 9
# Минимальное количество примеров
MIN_PRIM = 5  

# # # # # # # # # # # # # # # # #

# вывод версии игры
print(f"                        ")
print("\033[35m" + f"Версия игры = {ver}" + "\033[0m")
print(f"                        ")

# вывод танка)
print("▅███████ ]▄▄▄▄▄▄▄ ")
print("█████████▅▄▃ ")
print("Il███████████████████] ")
print("◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤")
print(f"                        ")

# Меню
def display_menu():
    print(f"                        ")
    print("\033[45m" + f"1. Умножение" + "\033[0m")
    print("\033[45m" + f"2. Вычитание" + "\033[0m")
    print("\033[45m" + f"3. Сложение" + "\033[0m")
    print("\033[45m" + f"4. Деление" + "\033[0m")
    print("\033[45m" + f"5. Выход" + "\033[0m")
    print(f"                        ")

# Обработки ошибок при вводе пользователем нечислового значения
# вместо prim = int(input())
# prim = get_integer_input("Введите количество примеров: ")
# n = get_integer_input("Введите ваш ответ: ")
def get_integer_input(prompt):
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Ошибка: Введите целое число.")

# Вариант 1 \ умножение
def option_1():
    print("Вы выбрали Вариант 1 - Умножение")

    prav = 0  # количество правильных ответов
    neprav = 0  # количество не правильных ответов

    prim = get_integer_input("Введите количество примеров сколько ты хочешь решить: ")
    if prim < MIN_PRIM:
        print(f"Как то мало, давай хотя бы {MIN_PRIM})")
        prim = MIN_PRIM

    print(f"                        ")

    # умножение
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        for i in range(1, prim + 1):
            a = random.randint(MIN_OPERAND_MULTIPLICATION, MAX_OPERAND_MULTIPLICATION)  # случайное целое число N, A ≤ N ≤ B.
            b = random.randint(MIN_OPERAND_MULTIPLICATION, MAX_OPERAND_MULTIPLICATION)  # случайное целое число N, A ≤ N ≤ B.
            m = a * b

            print("\033[30;47;1m" + f"Вопрос {i} из {prim}" + "\033[0m")
            print(f"Сколько будет {a} умножить на {b}?")
            n = get_integer_input("Введите ваш ответ: ")
            if m == n:
                prav = prav + 1
                print(
                    "\033[32m"
                    + f"Молодец! Это твой {prav} правильный ответ."
                    + "\033[0m"
                )
            else:
                neprav = neprav + 1
                print(
                    "\033[33m"
                    + f"Ты ошибся, правильный ответ будет {m}. Это твой {neprav} неправильный ответ"
                    + "\033[0m"
                )
                # запись в файлик
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} | Вопрос - {a} умножить на {b} : {m} (Правильный ответ) - {n} (Неправильный ответ)\n"
                file.write(data)
            print(f"                        ")

    # итог
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        print(f"                        ")
        print("\033[30;47;1m" + f"Итог" + "\033[0m")
        print(f"Ты решил {prim} примеров")
        if prav != 0:
            print(f"Из них правильных было {prav}")
        else:
            print(f"И не одного правильного(")

        if neprav != 0:
            print(f"А не правильных было {neprav}")
        else:
            print(f"И не одного неправильного, ты молодец!")
        print()
        # запись в файлик
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{timestamp} | Решено - {prim} - тема - умножение\n"
        file.write(data)


# Вариант 2 \ вычитание
def option_2():
    print("Вы выбрали Вариант 2 - Вычитание")
    prav = 0  # количество правильных ответов
    neprav = 0  # количество не правильных ответов

    prim = get_integer_input("Введите количество примеров сколько ты хочешь решить: ")
    if prim < MIN_PRIM:
        print(f"Как то мало, давай хотя бы {MIN_PRIM})")
        prim = MIN_PRIM

    print(f"                        ")

    # вычитание
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        for i in range(1, prim + 1):
            a = random.randint(MIN_OPERAND_SUBTRACTION, MAX_OPERAND_SUBTRACTION)  # случайное целое число N, A ≤ N ≤ B.
            b = random.randint(MIN_OPERAND_SUBTRACTION, MAX_OPERAND_SUBTRACTION)  # случайное целое число N, A ≤ N ≤ B.

            if a < b:  # если a меньше b - меняем местами
                a, b = b, a
            elif a == b:  # если a равно b - вычитаем 1
                b = b - 1

            m = a - b  # надо - a больше b

            print("\033[30;47;1m" + f"Вопрос {i} из {prim}" + "\033[0m")
            print(f"Сколько будет из {a} вычесть {b}?")
            n = get_integer_input("Введите ваш ответ: ")
            if m == n:
                prav = prav + 1
                print(
                    "\033[32m"
                    + f"Молодец! Это твой {prav} правильный ответ."
                    + "\033[0m"
                )
            else:
                neprav = neprav + 1
                print(
                    "\033[33m"
                    + f"Ты ошибся, правильный ответ будет {m}. Это твой {neprav} неправильный ответ"
                    + "\033[0m"
                )
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} | Вопрос - из {a} вычесть {b} : {m} (Правильный ответ) - {n} (Неправильный ответ)\n"
                file.write(data)
            print(f"                        ")

    # итог
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        print(f"                        ")
        print("\033[30;47;1m" + f"Итог" + "\033[0m")
        print(f"Ты решил {prim} примеров")
        if prav != 0:
            print(f"Из них правильных было {prav}")
        else:
            print(f"И не одного правильного(")

        if neprav != 0:
            print(f"А не правильных было {neprav}")
        else:
            print(f"И не одного неправильного, ты молодец!")
        print()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{timestamp} | Решено - {prim} - тема - вычитание\n"
        file.write(data)


# Вариант 3 \ сложение
def option_3():
    print("Вы выбрали Вариант 3 - Сложение")

    prav = 0  # количество правильных ответов
    neprav = 0  # количество не правильных ответов

    prim = get_integer_input("Введите количество примеров сколько ты хочешь решить: ")
    if prim < MIN_PRIM:
        print(f"Как то мало, давай хотя бы {MIN_PRIM})")
        prim = MIN_PRIM

    print(f"                        ")

    # сложение
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        for i in range(1, prim + 1):
            a = random.randint(MIN_OPERAND_ADDITION, MAX_OPERAND_ADDITION)  # случайное целое число N, A ≤ N ≤ B.
            b = random.randint(MIN_OPERAND_ADDITION, MAX_OPERAND_ADDITION)  # случайное целое число N, A ≤ N ≤ B.

            m = a + b  # надо - a больше b

            print("\033[30;47;1m" + f"Вопрос {i} из {prim}" + "\033[0m")
            print(f"Сколько будет {a} прибавить к {b}?")
            n = get_integer_input("Введите ваш ответ: ")
            if m == n:
                prav = prav + 1
                print(
                    "\033[32m"
                    + f"Молодец! Это твой {prav} правильный ответ."
                    + "\033[0m"
                )
            else:
                neprav = neprav + 1
                print(
                    "\033[33m"
                    + f"Ты ошибся, правильный ответ будет {m}. Это твой {neprav} неправильный ответ"
                    + "\033[0m"
                )
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} | Вопрос - {a} прибавить к {b} : {m} (Правильный ответ) - {n} (Неправильный ответ)\n"
                file.write(data)
            print(f"                        ")

    # итог
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        print(f"                        ")
        print("\033[30;47;1m" + f"Итог" + "\033[0m")
        print(f"Ты решил {prim} примеров")
        if prav != 0:
            print(f"Из них правильных было {prav}")
        else:
            print(f"И не одного правильного(")

        if neprav != 0:
            print(f"А не правильных было {neprav}")
        else:
            print(f"И не одного неправильного, ты молодец!")
        print()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{timestamp} | Решено - {prim} - тема - сложение\n"
        file.write(data)


# Вариант 4 \ деление
def option_4():
    print("Вы выбрали Вариант 4 - Деление")
    prav = 0  # количество правильных ответов
    neprav = 0  # количество не правильных ответов

    prim = get_integer_input("Введите количество примеров сколько ты хочешь решить: ")
    if prim < MIN_PRIM:
        print(f"Как то мало, давай хотя бы {MIN_PRIM})")
        prim = MIN_PRIM

    print(f"                        ")
    # вычитание
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        for i in range(1, prim + 1):
            a = random.randint(MIN_OPERAND_SUBTRACTION, MAX_OPERAND_SUBTRACTION)  # случайное целое число N, A ≤ N ≤ B.
            b = random.randint(MIN_OPERAND_SUBTRACTION, MAX_OPERAND_SUBTRACTION)  # случайное целое число N, A ≤ N ≤ B.

            m = a * b

            print("\033[30;47;1m" + f"Вопрос {i} из {prim}" + "\033[0m")
            print(f"Сколько будет {m} поделить на {a}?")
            n = get_integer_input("Введите ваш ответ: ")
            if b == n:
                prav = prav + 1
                print(
                    "\033[32m"
                    + f"Молодец! Это твой {prav} правильный ответ."
                    + "\033[0m"
                )
            else:
                neprav = neprav + 1
                print(
                    "\033[33m"
                    + f"Ты ошибся, правильный ответ будет {b}. Это твой {neprav} неправильный ответ"
                    + "\033[0m"
                )

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                data = f"{timestamp} | Вопрос - {m} поделить на {a} : {b} (Правильный ответ) - {n} (Неправильный ответ)\n"
                file.write(data)

            print(f"                        ")

    # итог
    with open("ответы.txt", "a") as file:  # открываем файлик режиме Add
        print(f"                        ")
        print("\033[30;47;1m" + f"Итог" + "\033[0m")
        print(f"Ты решил {prim} примеров")
        if prav != 0:
            print(f"Из них правильных было {prav}")
        else:
            print(f"И не одного правильного(")

        if neprav != 0:
            print(f"А не правильных было {neprav}")
        else:
            print(f"И не одного неправильного, ты молодец!")
        print()
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f"{timestamp} | Решено - {prim} - тема - деление\n"
        file.write(data)



def main():
    while True:
        display_menu()
        choice = input("Выберите вариант: ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()
