# 1.
# def func_a():
#     print("Step 2", end=" ")
#
# def func_b():
#     print("Step 5", end=" ")
#
# def func_c():
#     print("Step 3", end=" ")
#
# def func_d():
#     print("Step 4", end=" ")
#
# def func_e():
#     print("Step 1", end=" ")
#
# func_e()
# func_a()
# func_c()
# func_d()
# func_b()


# def func_a():
#     print("Step 4", end=" ")
#
# def func_b():
#     print("Step 1", end=" ")
#
# def func_c():
#     print("Step 3", end=" ")
#
# def func_d():
#     print("Step 2", end=" ")
#
# def func_e():
#     print("Step 5", end=" ")
#
# func_e()
# func_a()
# func_c()
# func_d()
# func_b()





# 2.
# def func_a():
#     print("Step 5.", end=" ")
#
# def func_b():
#     print("Step 1.", end=" ")
#
# def func_c():
#     print("Step 2.", end=" ")
#
# def func_d():
#     print("Step 4.", end=" ")
#
# def func_e():
#     print("Step 3.", end=" ")
#
# func_b()
# func_c()
# func_e()
# func_d()
# func_a()
#
#
# func_a()
# func_d()
# func_e()
# func_c()
# func_b()


# 3.

# def func_a():
#     print("Step 7", end=" ")
#
# def func_b():
#     print("Step 3", end=" ")
#
# def func_c():
#     print("Step 4", end=" ")
#
# def func_d():
#     print("Step 1", end=" ")
#
# def func_e():
#     print("Step 6", end=" ")
#
# func_d()
# print("Step 2", end=" ")
# func_b()
# func_c()
# print("Step 5", end=" ")
# func_e()
# func_a()
#
# def func_a():
#     print("Step 1", end=" ")
#
# def func_b():
#     print("Step 5", end=" ")
#
# def func_c():
#     print("Step 4", end=" ")
#
# def func_d():
#     print("Step 7", end=" ")
#
# def func_e():
#     print("Step 2", end=" ")
#
# func_d()
# print("Step 6", end=" ")
# func_b()
# func_c()
# print("Step 3", end=" ")
# func_e()
# func_a()



# 4.
# def func_a():
#     print("Step 5", end=" ")
#
# def func_b():
#     print("Step 1", end=" ")
#
# def func_c():
#     func_b()
#     print("Step 2", end=" ")
#
# def func_d():
#     print("Step 7", end=" ")
#
# def func_e():
#     print("Step 4", end=" ")
#     func_a()
#
# func_c()
# print("Step 3", end=" ")
# func_e()
# print("Step 6", end=" ")
# func_d()
#
# def func_a():
#     print("Step 3", end=" ")
#
# def func_b():
#     print("Step 7", end=" ")
#
# def func_c():
#     func_b()
#     print("Step 6", end=" ")
#
# def func_d():
#     print("Step 1", end=" ")
#
# def func_e():
#     print("Step 4", end=" ")
#     func_a()
#
# func_c()
# print("Step 5", end=" ")
# func_e()
# print("Step 2", end=" ")
# func_d()

# 5.

# def func_a():
#     print("Step 2.", end=" ")
#
# def func_b():
#     print("Step 3.", end=" ")
#
# def func_c():
#     func_b()
#     print("Step 4.", end=" ")
#
# def func_d():
#     print("Step 5.", end=" ")
#
# def func_e():
#     print("Step 1.", end=" ")
#     func_a()

# func_e()
# func_c()
# func_d()


# 6.
# PC:  - Buy a fur coat!
# You: - I will not
# PC:  - Everyone says: "I will not", but you buy a fur coat!
# You: -
# PC:  - Everyone is silent, but you buy a fur coat!
# You: - Give me money.
# PC:  - Everyone says: "Give me money," but you buy a fur coat!
# You: - Good.
# PC:  - Everyone says "Good", but you buy a fur coat!
# ...



# def var_one():
#     print("PC: - Everyone says: {}, but you buy a fur coat!".format(text).)#двойные пробелы поправить
#
# def var_two():
#     print("PC: - Everyone is silent, but you buy a fur coat!")
#
# def var_three():
#     print("PC: - Everyone says: {}, but you buy a fur coat!".format(text))
#
# def var_four():
#     print("PC: - Everyone says: {}, but you buy a fur coat!".format(text))
#
# def var_five():
#   print("PC: - Everyone says: {}, but you buy a fur coat!".format(text))
#
# def var_six():
#     print("PC: - Everyone says: {}, but you buy a fur coat!".format(text))
#
# def var_seven():
#     print("PC: - Everyone says: {}, but you buy a fur coat!".format(text))
#
# text = input("PC: - Buy a fur coat!")
#
# if text == 'I will not':
#     var_one()
# elif text == '':
#     var_two()
# elif text == 'Give me money':
#     var_three()
# elif text == 'Good':
#     var_four()
# elif text == 'Stfu':
#     var_five()
# elif text == 'Ok-ok':
#     var_six()
# elif text == 'Maybe':
#     var_seven()
# else:
#     print("Задолбал меня страшно")


def buy_fur_coat():
    print('PC: - Buy a fur coat!')
    answer = input('You: - ').strip()

    if answer: # не сравниваем с пустотой
        print('PC: - Everyone is silent, but you buy a fur coat!')
    else:
        print(f'PC: - Everyone says: "{answer}", but you buy a fur coat!')

buy_fur_coat()
buy_fur_coat()
buy_fur_coat()
buy_fur_coat()
buy_fur_coat()
buy_fur_coat()
buy_fur_coat()


# 7.
# Основная ветка программы, не считая заголовков функций, состоит из одной строки кода. Это вызов функции test().
#
# В функции test() запрашивается на ввод целое число. Если число положительное, то вызывается функция positive(), если число отрицательное, то вызывается функция negative().
# тело функции positive() содержит команду вывода в консоль слово "Положительное".
# тело функции negative() выводит в консоль слово "Отрицательное".
# Имеет ли значение порядок определения самих функций? То есть должны ли определения positive() и negative() предшествовать test() или должны следовать после него? Проверьте вашу гипотезу, поменяв функций местами. Попробуйте объяснить результат.


def positive():
    print("Number is positive")
def negative():
    print("Number is negative")
def test():
    a = int(input("Please input number:"))
    positive() if a>0 else negative()
test()

