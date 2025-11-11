# line_input = input("Input text:")
# if line_input != "":
#     print("OK")


# Напишите программу, которая запрашивает у пользователя целое число. Если оно больше нуля,
# то в ответ на экран выводится число 1.
# Если введенное число не является положительным, то на экран должно выводиться -1.
# line_input = int(input("Input integer:"))
# if line_input > 0:
#     print(1)
# elif line_input < 0:
#     print(-1)



#  Напишите программу, в которой у пользователя спрашивается: "What time is it?" и принимает на ввод только число часов от 0 до 24. В зависимости от введенного числа часа, программа выводит:

# с 4 по 11 - "Good morning!"
# с 12 по 16 - "Good afternoon!"
# с 17 по 22 - "Good evening!"
# с 23 до 3 - "Good night!"

# line_input = int(input("What time is it?:"))
# if 4 <= line_input <= 11:
#     print("Good morning!")
# elif 12 <=  line_input <= 16:
#     print("Good afternoon!")
# elif 17 <=  line_input <= 22:
#     print("Good evening!!")
# elif  line_input == 23 or 0 <= line_input <= 3:
#     print("Good night!")
# else:
#     print('Error')


# Напишите программу, которая спрашивает у пользователя: "What season of year is it?" Ввод: "winter", "spring", "summer", "autumn" или "fall". В зависимости от введенного значения, программа предлагает вам одеть на себя один из предметов одежды по сезону. Если введенные данные неизвестны программе, сообщается об ошибке ввода.
# line_input = input("What season of year is it?:").strip().lower()
# if line_input == "winter" :
#     print("Put on puffer jacket")
# elif line_input == "spring" :
#     print("Put on spring coat")
# elif line_input == "summer" :
#     print("Put on summer dress")
# elif line_input == "autumn" or line_input == "fall" :
#     print("Put on rubber shoes")
# else:
#     print('Error')

#Напишите программу "ЭХО". Программа выводит сообщение пользователю PC: - Enter`` any text. Если пользователь вводит текст, то ПК отвечает: PC: - You said: "<user text>". Если пользователь ввел пустоту (просто нажал клавишу Enter), то программа выводит PC: - You are still silent. Диалог длится пять повторений.

for i in range(5):
    line_input = input("PC: - Enter any text: ")
    if line_input != "":
        print(f'PC: - You said:"{line_input}"')
    else:
        print("PC: - You are still silent.")







