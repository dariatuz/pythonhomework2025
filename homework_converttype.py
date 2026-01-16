# При решении упражнений в логических выражениях допускается преобразование только к строке и логическому типу.
#
# Проверка пустой строки
#
# Считай строку.
# Если строка пустая → вывести "You didn't enter anything", иначе "Thank you for your input".
# Проверка целого числа на диапазон
from PIL.ImImagePlugin import number

# line = input("Введи строку:")
# # if line == "" :
# # if bool(line):
# if not line:
#     print("You didn't enter anything")
# else:
#     print("Thank you for your input")


# Пользователь вводит число.
# Если число в диапазоне от 0 до 9 включительно → "OK", иначе "Out of range".
# number = input("Input number please: ")

# if "0" <= number <= "9":
# if 0 <= int(number) <= 9:
# if bool("0" <= number <= "9"):
#
#     print("OK")
# else:
#     print("Out of range")


# Булево выражение из строки#





# Проверка логина и пароля
#
# Пользователь вводит логин и пароль.
# Если пользователь ничего не ввел вывести: "Data is empty"
# Если логин и пароль введены и не содержат пробелов → "Login successful".
# Иначе "Authentication failed".


# login = input("Input login:")
# password = input("input password:")
#
# if not login or not password:
#     print("Data is empty")
# elif " " not in login and " " not in password:
#     print("Login successful")
# else:
#     print("Authentication failed")

# Проверка строки на пустоту и длину
#
# Пользователь вводит строку.
# Если строка пустая → "Empty string".
# Если длина строки > 5 → "Long string".
# Иначе "Short string".

# line = input("Input line:")
# if not line:
#     print("Empty string")
# elif len(line)>5:
#     print("Long string")
# else:
#     print("Short string")




# Проверка целого положительного числа на чётность
#
# Пользователь вводит число.
# Если число > 0 и чётное → "Positive even number".
# Если число > 0 и нечётное → "Positive odd number".
# Если не число "Not a positive number".
# Калькулятор деления

# line = input("Please input number:").strip()
# if not line.isnumeric():
#     print("Not a positive number")
# elif line.endswith("0") or line.endswith("2") or line.endswith(("4","6","8")):
#     print("Positive even number")
# else:
#     print("Positive odd number")

# Калькулятор деления
#
# Пользователь вводит два целых положительных числа
# Пользователь вводит операцию: /, //, %.
# Выполни операцию и выведи результат, не более трех знаков после запятой.
# Если пользователь вводит неверные данные вывести сообщение: "Incorrect data..."


number_one = input("Please input first number:")
number_two = input("Please input second number:")
number_three = input("Please input /, //, %.:")

if numberTwo == "0":
    print("Incorrect data...")

elif operation  == "/":
    result = number_one // number_three
    print(f"{result:.3f}")

elif operation == "//":
    result = number_one  // number_two
    print(result)

elif operation == "%":
    result = number_one % number_two
    print(result)

else:
    print("Incorrect data...")

