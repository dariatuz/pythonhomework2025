"""1.Используя метод grid() напишите программу состоящую из:

однострочного текстового поля,
метки с отображением знака "+",
второго однострочного текстового поля,
кнопкой "=", при нажатии на которую результат вычисления выводиться в третье текстовое поле,
третьего однострочного тестового поля."""


from tkinter import*


def sumup():
    # print(leftfield_sum.get() == 0,centralfield_sum.get() == 0)
    if not leftfield_sum.get()   and centralfield_sum.get():
    # if leftfield_sum.get().strip() and centralfield_sum.get().strip():
        a = float(leftfield_sum.get())
        b = float(centralfield_sum.get())
        sum_result = a + b
        # print(result)
        text_field_right_sum.delete(0, END)
        text_field_right_sum.insert(END,str(sum_result))


def subtract():
    if leftfield_subtraction.get().strip() and centralfield_subtraction.get().strip():
        a = float(leftfield_subtraction.get())
        b = float(centralfield_subtraction.get())
        subtraction_result = a - b
        # print(result)
        text_field_right_subtraction.delete(0, END)
        text_field_right_subtraction.insert(END,str(subtraction_result))

def multiply():
    if leftfield_multiplication.get().strip() and centralfield_multiplication.get().strip():
        a = float(leftfield_multiplication.get())
        b = float(centralfield_multiplication.get())
        multiplication_result = a * b
        # print(result)
        text_field_right_multiplication.delete(0, END)
        text_field_right_multiplication.insert(END,str(multiplication_result))


def raise_to_exponent():
    if leftfield_exponentiation.get().strip() and centralfield_exponentiation.get().strip():
        a = float(leftfield_exponentiation.get())
        b = float(centralfield_exponentiation.get())
        exponentiation_result = a ** b
        # print(result)
        text_field_right_exponentiation.delete(0, END)
        text_field_right_exponentiation.insert(END,str(exponentiation_result))


def divide():
    if leftfield_division.get().strip() and centralfield_division.get().strip():
        a = float(leftfield_division.get())
        b = float(centralfield_division.get())
        division_result = int(a / b)
        # print(result)
        text_field_right_division.delete(0, END)
        text_field_right_division.insert(END,str(division_result))

def floor_divide():
    print(leftfield_floor_division.get().strip() =="0" , centralfield_floor_division.get().strip()!="0")
    if not leftfield_floor_division.get().strip() =="0" and centralfield_floor_division.get().strip()!="0":
        a = float(leftfield_floor_division.get().strip())
        b = float(centralfield_floor_division.get().strip())
        division_result = a // b
        # print(result)
        text_field_right_floor_division.delete(0, END)
        text_field_right_floor_division.insert(END,str(division_result))

def modulo():
    if not leftfield_floor_division.get().strip() and centralfield_floor_division.get().strip:
        a = float(leftfield_modulo.get())
        b = float(centralfield_modulo.get())
        modulo_result = a % b
    # print(result)
        text_field_right_modulo.delete(0, END)
        text_field_right_modulo.insert(END, str(modulo_result))



root = Tk()
root.title("Welcome to grid app!")
root.geometry('350x200')

leftfield_sum = StringVar()
text_field_left_sum = Entry(root, width=10,textvariable=leftfield_sum, bg="white", fg="black")
text_field_left_sum.grid(row=0, column=1)

label_addition = Label(text="+")
label_addition.grid(row=0, column=2)

centralfield_sum = StringVar()
text_field_central_sum = Entry(root, width=10,textvariable=centralfield_sum, bg="white", fg="black",)
text_field_central_sum.grid(row=0, column=3)

button_equal_sign_sum = Button(root, text="=", bg="white", fg="black", command=sumup)
button_equal_sign_sum.grid(row=0, column=4)

text_field_right_sum = Entry(root, width=10, bg="white", fg="black",)
text_field_right_sum.grid(row=0, column=5)



leftfield_subtraction = StringVar()
text_field_left_subtraction = Entry(root, width=10,textvariable=leftfield_subtraction, bg="white", fg="black")
text_field_left_subtraction.grid(row=1, column=1)

label_subtraction = Label(text="-")
label_subtraction.grid(row=1, column=2)

centralfield_subtraction = StringVar()
text_field_central_subtraction  = Entry(root, width=10,textvariable=centralfield_subtraction, bg="white", fg="black",)
text_field_central_subtraction.grid(row=1, column=3)

button_equal_sign_subtraction = Button(root, text="=", bg="white", fg="black", command=subtract)
button_equal_sign_subtraction.grid(row=1, column=4)

text_field_right_subtraction = Entry(root, width=10, bg="white", fg="black",)
text_field_right_subtraction.grid(row=1, column=5)


leftfield_multiplication = StringVar()
text_field_left_multiplication= Entry(root, width=10,textvariable=leftfield_multiplication, bg="white", fg="black")
text_field_left_multiplication.grid(row=2, column=1)

label_multiplication= Label(text="*")
label_multiplication.grid(row=2, column=2)

centralfield_multiplication = StringVar()
text_field_central_multiplication  = Entry(root, width=10,textvariable=centralfield_multiplication, bg="white", fg="black",)
text_field_central_multiplication.grid(row=2, column=3)

button_equal_sign_multiplication = Button(root, text="=", bg="white", fg="black", command=multiply)
button_equal_sign_multiplication.grid(row=2, column=4)

text_field_right_multiplication = Entry(root, width=10, bg="white", fg="black",)
text_field_right_multiplication.grid(row=2, column=5)


leftfield_exponentiation  = StringVar()
text_field_left_exponentiation = Entry(root, width=10,textvariable=leftfield_exponentiation, bg="white", fg="black")
text_field_left_exponentiation.grid(row=3, column=1)

label_exponentiation = Label(text="**")
label_exponentiation .grid(row=3, column=2)

centralfield_exponentiation = StringVar()
text_field_central_exponentiation  = Entry(root, width=10,textvariable=centralfield_exponentiation, bg="white", fg="black",)
text_field_central_exponentiation.grid(row=3, column=3)

button_equal_sign_exponentiation = Button(root, text="=", bg="white", fg="black", command=raise_to_exponent)
button_equal_sign_exponentiation.grid(row=3, column=4)

text_field_right_exponentiation= Entry(root, width=10, bg="white", fg="black",)
text_field_right_exponentiation.grid(row=3, column=5)


leftfield_division  = StringVar()
text_field_left_division = Entry(root, width=10,textvariable=leftfield_division, bg="white", fg="black")
text_field_left_division.grid(row=4, column=1)

label_division = Label(text="/")
label_division.grid(row=4, column=2)

centralfield_division = StringVar()
text_field_central_division  = Entry(root, width=10,textvariable=centralfield_division, bg="white", fg="black",)
text_field_central_division.grid(row=4, column=3)

button_equal_sign_division = Button(root, text="=", bg="white", fg="black", command=divide)
button_equal_sign_division.grid(row=4, column=4)

text_field_right_division= Entry(root, width=10, bg="white", fg="black",)
text_field_right_division.grid(row=4, column=5)


leftfield_floor_division  = StringVar()
text_field_left_floor_division = Entry(root, width=10,textvariable=leftfield_floor_division, bg="white", fg="black")
text_field_left_floor_division.grid(row=5, column=1)

label_division_floor_division = Label(text="//")
label_division_floor_division.grid(row=5, column=2)

centralfield_floor_division = StringVar()
text_field_central_floor_division  = Entry(root, width=10,textvariable=centralfield_floor_division, bg="white", fg="black",)
text_field_central_floor_division.grid(row=5, column=3)

button_equal_sign_floor_division = Button(root, text="=", bg="white", fg="black", command=floor_divide)
button_equal_sign_floor_division.grid(row=5, column=4)

text_field_right_floor_division= Entry(root, width=10, bg="white", fg="black",)
text_field_right_floor_division.grid(row=5, column=5)


leftfield_modulo= StringVar()
text_field_left_modulo = Entry(root, width=10,textvariable=leftfield_modulo, bg="white", fg="black")
text_field_left_modulo.grid(row=6, column=1)

label_modulo = Label(text="%")
label_modulo.grid(row=6, column=2)

centralfield_modulo = StringVar()
text_field_central_modulo  = Entry(root, width=10,textvariable=centralfield_modulo, bg="white", fg="black",)
text_field_central_modulo.grid(row=6, column=3)

button_equal_sign_modulo = Button(root, text="=", bg="white", fg="black", command=modulo)
button_equal_sign_modulo.grid(row=6, column=4)

text_field_right_modulo= Entry(root, width=10, bg="white", fg="black",)
text_field_right_modulo.grid(row=6, column=5)



root.mainloop()