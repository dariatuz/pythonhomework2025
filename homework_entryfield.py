# 1.Создайте окно с текстовым полем Entry, и задайте значение текстового поля: «Текстовое поле вводит и выводит текст только одной строкой», используя метод .

# from tkinter import *
# from tkinter.ttk import Entry#Подключи набор инструментов для рисования окон и кнопок = Импортируется модуль tkinter, который предоставляет классы и функции для создания графического интерфейса пользователя, The tkinter module is imported, which provides classes and functions for creating a graphical user interface.
# root = Tk() # создаем главное окно программы.
# #root — это переменная, в которой хранится это окно.
# root.title("tk")
# text = Entry(root, width=50)  # Создаём поле ввода текста
# text.insert(0,"Текстовое поле вводит и выводит текст только одной строкой")
# text.pack()
# root.mainloop()



# from tkinter import *
#
# root = Tk()
# root.title("tk")
# root.geometry("900x120")
#
# e = Entry(root, width=80)
# e.pack(padx=10, pady=20)
#
# e.insert(0, "Текстовое поле вводит и выводит текст только одной строкой")
#
# root.mainloop()

# from tkinter import *
# from tkinter import messagebox
#
# def display_full_name():
#     messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

# root = Tk()
# root.title("GUI на Python")
#
# name_label = Label(text="Введите имя:")
# name_label.grid(row=0, column=0, sticky="w")
# name = StringVar()
# name_entry = Entry(textvariable=name)
# name_entry.grid(row=0, column=1)
#
# surname_label = Label(text="Введите фамилию:")
# surname_label.grid(row=1, column=0, sticky="w")
# surname = StringVar()
# surname_entry = Entry(textvariable=surname)
# surname_entry.grid(row=1, column=1)
#
# message_button = Button(text="Click Me", command=display_full_name)
# message_button.grid(row=2, column=1)
#
# root.mainloop()



# 2. Используя переменную StringVar(). Создайте окно с текстовым полем и двумя кнопками:

# кнопкой "Paste", при нажатии на которую, в текстовом поле выводится текст: "The button clicked!".
# кнопкой "Clear", при нажатии на которую, текст в текстовом поле стирается.
# from tkinter import *
#
# def paste_text():
#     text.set("The button clicked")
# def clear_entry():
#     # entry.delete(0,END)
#     text.set("")
#
#
# root = Tk()# creating a parent window
# root.title ("Tk")
#
# text = StringVar()#Создаётся переменная StringVar для хранения текста.
# entry = Entry(root, width=50, textvariable=text)# Создаётся поле ввода шириной ~50 символов внутри root.
# entry.pack()
#
# button1 = Button(root, text = "Paste", command = paste_text)
# button1.pack()
# button2 = Button(root,text = "Clear", command = clear_entry)
# button2.pack()
#
# root.mainloop()



# 3. Используя методы .insert() и .delete() для текстового поля. Создайте окно с текстовым полем и двумя кнопками:
# кнопкой "Paste", при нажатии на которую, в текстовом поле выводится текст: "The button clicked!".
# кнопкой "Clear", при нажатии на которую, текст в текстовом поле стирается.


# from tkinter import *  # Import all classes, functions, and constants from tkinter

#тут тоже 2 пробела
# def clear_text():
#     entry.delete(0, END)
#
# # функции отделяются 2мя пробелами
# def paste_text():
#     entry.insert(0,"The button clicked")

# Create the main application window
# root = Tk() # This line creates the main application window. #All other widgets will be placed inside this window.
# root.title("tk")
#
# # Create Entry widget
# entry = Entry(root, width=50) # Я создала переменную ent и присвоила ей результат вызова Entry(root), где Entry — это класс Tkinter, создающий элемент интерфейса, а root — главное окно, к которому этот элемент привязывается. ч#Я создала переменную ent и присвоила ей результат вызова Entry(root), где Entry — это класс Tkinter, создающий элемент интерфейса, а root — главное окно, к которому этот элемент привязывается. ent.pack()
# # ent.insert(0, "Tom")
# entry.pack()
#
# # Create buttons
# button_paste = Button(root, text="Paste", command = paste_text)
# button_paste.pack()
#
# button_clear = Button(root, text="Clear", command=clear_text)
# button_clear.pack()
#
# # Start the application
# root.mainloop()



#4.Используя переменную StringVar(). Создайте окно с текстовым полем и кнопкой "Copy", при нажатии на которую, выводится значение текстового поля в консоль.

# from tkinter import*
#
#
# def copy_text():
#     print(text.get())
#
# #функция с двух сторон выделяется двумя пустыми строками
# root = Tk()
# root.title("Tk")
#
# text = StringVar()
# entry = Entry(root, width=40, textvariable=text)
# entry.pack()
#
# button_copy = Button(root, text="Copy", command=copy_text)
# button_copy.pack()
#
# root.mainloop()


#5.Используя команды .get() для виджета текстового поля. Создайте окно с текстовым полем и кнопкой "Copy", при нажатии на которую, выводится значение текстового поля в консоль.
# from tkinter import*
#
#
# def copy_text():
#     print(entry.get())
#
#
# root = Tk()
# root.title("Tk")
#
# entry = Entry(root, width=40)
# entry.pack()
#
# button_copy = Button(root, text="Copy", command=copy_text)
# button_copy.pack()
# root.mainloop()



# 6.

#Создайте программу с двумя текстовыми полями и двумя кнопками.
#при нажати на первую кнопку, должны выводиться значения первого и второго полей в консоль:
#при нажатии на вторую кнопку, должны выводиться значения первого и второго полей в консоль с пояснениями в виде:


# from tkinter import*
#
#
# def print_text_raw():
#     print(f"{entry_1.get()}\n{entry_2.get()}")
#
#
# def print_text_format():
#     print(f"Значение первого поля:<{entry_1.get()}>")
#     print(f"Значение второго поля:<{entry_2.get()}>")
#
#
# root = Tk()
#
# entry_1 = Entry(root, width=40)
# entry_1.pack()
# entry_2 = Entry(root, width= 40)
# entry_2.pack()
#
# button_text_raw = Button(root, text="Print text raw", command=print_text_raw)
# button_text_raw.pack()
# button_text_format = Button(root, text="Print text format", command=print_text_format)
# button_text_format.pack()
#
# root.mainloop()

# 7.Создайте окно с двумя однострочными текстовыми полями и кнопкой, при нажатии на которую, значение первого текстового поля будет выводиться во втором текстовом поле.

# from tkinter import*
#
#
# def copy_text():
#     entry_2.delete(0,END)
#     entry_2.insert(0, entry_1.get())
#
#
# root = Tk()
# root.title("Tk")
#
# entry_1 = Entry(root, width=40)
# entry_1.pack()
# entry_2 = Entry(root, width= 40)
# entry_2.pack()
#
# button_copy = Button(root, text="Copy", command=copy_text)
# button_copy.pack()
# root.mainloop()

# 8.Создайте окно с двумя однострочными текстовыми полями и кнопкой, при нажатии на которую, значение первого текстового поля будет выводиться во втором текстовом поле, с примечанием: «<текст первого поля>», - it is the first entry's contents.

# from tkinter import*
#
#
# def copy_text():
#     text = entry_input.get()
#     entry_output.delete(0, END)
#
#     # проверка пустоты
#     if text.strip():
#         entry_output.insert(0, f'"{text}" - it is the first entry\'s contents')
#     else:
#         entry_output.insert(0, "Поле ввода пустое!")
#
# root = Tk()
# root.title("Tk")
#
# entry_input = Entry(root, width=40)
# entry_input.pack()
#
# button_copy = Button(root, text="Copy", command=copy_text)
# button_copy.pack()
#
# entry_output = Entry(root, width= 40)
# entry_output.pack()
#
# root.mainloop()

 # 9.Создайте окно с тремя однострочными текстовыми полями и кнопкой, при нажатии на которую, значения первого и второго текстовых полей будут выводиться в третьем текстовом поле.

from tkinter import*


def copy_text():
    entry_output.delete(0, END)
    # entry_output.insert(0,entry_input_one.get() + entry_input_two.get())
    entry_output.insert(0,f"{entry_input_1.get()} {entry_input_2.get()}")


root = Tk()
entry_input_1 = Entry(root, width=40)
entry_input_1.pack()
entry_input_2 = Entry(root, width=40)
entry_input_2.pack()

button_copy = Button(root, text="Copy", command=copy_text)
button_copy.pack()

entry_output = Entry(root, width= 40)
entry_output.pack()

root.mainloop()