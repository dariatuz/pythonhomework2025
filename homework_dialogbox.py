# import tkinter as tk
# from tkinter import messagebox
#
# root = tk.Tk()
# root.withdraw()  # Скрываем основное окно
#
# messagebox.showinfo("Message title", "Message info content")
# root.mainloop()


# from tkinter import messagebox
#
# messagebox.showwarning('Message warning title', 'Message warning content') # show warning message


# from tkinter import messagebox
#
# messagebox.showerror('Message error title', 'Message error content')
#
#
# from tkinter import messagebox
#
# response = messagebox.askquestion('Message title', 'Message ask content')
# # просто вопрос с выбором без специфики ответа
# print(response)
# response = messagebox.askyesno('Message title', 'Message y/n content')
# # вопрос с выбором да/нет
# print(response)
# response = messagebox.askyesnocancel('Message title', 'Message y/n/cancel content')
# print(response)
# # вопрос с выбором да/нет/отмена
# response = messagebox.askokcancel('Message title', 'Message ok/cancel content')
# print(response)
# # вопрос с выбором ok/cancel
# response = messagebox.askretrycancel('Message title', 'Message retry/cancel content')
# print(response)
# # вопрос с выбором retry/cancel

# from tkinter import *
# from tkinter import filedialog
#
# root = Tk()
# document_open = filedialog.askopenfilename()
# document_save = filedialog.asksaveasfilename()
#
# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog
# root = tk.Tk()
# root.withdraw()
#
# print("Выбери 1 файл:")
# file1 = filedialog.askopenfilename()
# print("Выбранный файл:", file1)


# from tkinter import filedialog as fd
# filename = fd.askopenfilename()


import tkinter as tk
from tkinter import filedialog #вызываем подмодуль tkinter, который содержит функции для работы с файлами через диалоговые окна.


# file_path = filedialog.askopenfilename(title="Выберите файл")
# print(file_path) # askopenfilename возвращает в ответе путь к файлу
#
#
# file_paths = filedialog.askopenfilenames(title="Выберите файлы")
# print(file_paths)# askopenfilenames возвращает в ответе несколько путей к нескольким файлам
#
#
# file_object = filedialog.askopenfile(title="Выберите файл", mode='r')
# print(file_object)# возвращает объект файла
# if file:
#     for line in file:
#         print(line.strip())  # Читаем построчно
#     file.close()
#
#
# filename = filedialog.asksaveasfilename(title="Сохранить как")
# print(filename) # сохраняем файл / Выбор пути для сохранения файла (возвращает путь).


# filename = filedialog.asksaveasfile(title="Сохранить как")
# print(filename)# сохраняем файл / Выбор пути для сохранения файла (возвращает обьект).
#
#
# filename = filedialog.askdirectory(title="Сохранить как")
# print(filename)