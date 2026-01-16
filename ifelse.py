# line_input = input("Input text:")
# if line_input != "":
# #     print("OK")
# from homework_logical_expressions import line_input

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

# for i in range(5):
#     line_input = input("PC: - Enter any text: ")
#     if line_input != "":
#         print(f'PC: - You said:"{line_input}"')
#     else:
#         print("PC: - You are still silent.")

#Напишите программу: "Buy a fur coat!" Программа подобие диалога:

#Программа выводит сообщение: "PC: - Buy a fur coat!"
#После программа ждет ответного ввода с клавиатуры, например: "You: - No".
#Далее программа выводит: PC: - Everyone says: "No", but you buy a fur coat!"
#Если пользователь ничего не вводит, только нажимает "Enter", то программа отвечает: "PC: - Everyone is silent, but you buy a fur coat!"
#Ответы могут быть другие, в произвольном порядке.
#Реализуйте 5 повторов в диалоге вопрос-ответ.
#Пример работы программы может быть следующим:

# for i in range(5):
#     line_input = input("PC: - Buy a fur coat!:")
#     if line_input == "No":
#         print('"PC: - Everyone says: "No", but you buy a fur coat!"')
#     elif line_input == "":
#         print("PC: - Everyone is silent, but you buy a fur coat!")

# for i in range(5):
#     firstuser_name = input("PC: - Please input first user name:")
#     seconduser_name = input("PC: - Please input second user name:")
#     if  firstuser_name ==  firstuser_name :
#         print(f'PC: - first user name is :"{firstuser_name}"')



# pc=input("Please, enter the first person's name: ").strip().capitalize()
# you=input("Please, enter the second person's name: ").strip().capitalize()
# w=max(len(pc),len(you))
# for _ in range(5):
#     print(f"{pc.ljust(w)}:  - Buy a fur coat!")
#     r=input(f"{you}: - ").strip()
#     print(f"""{pc.ljust(w)}:  - {'Everyone is silent' if not r else f'Everyone says: "{r}"'}, but you buy a fur coat!""")
# #for и max не использовать

# a,b,c=map(float,input("Введите три числа: ").split())
# m=a
# if b<m:m=b
# if c<m:m=c
# print("Минимум:",m)
#
# #map не использовать


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)


# # Считываем три целых числа
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
#
# # Находим наименьшее число
# min_number = min(a, b, c)
#
# # Выводим результат
# print("Наименьшее число:", min_number)


number_user = int(input())
number_min = number_user

number_user = int(input())
if number_user < number_min:
    number_min = number_user

number_user = int(input())
if number_user < number_min:
    number_min = number_user

number_user = int(input())
if number_user < number_min:
    number_min = number_user

print(number_min)





