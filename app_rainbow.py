"""1.  Напишите программу с заголовком "Colors" и меткой с текстом «Color name»,
размер шрифта для всех виджетов можно указать font=20:
Добавьте в программу одно-строчное текстовое поле с текстом «Color code».
Выровняйте текст по центру текстового поля, используя свойство justify=CENTER
Добавьте в программу 7 кнопок, цвета которых соответствуют цветам радуги. Коды цветов в шестнадцатеричной кодировке:
#ff0000 – красный (red),
#ff7d00 – оранжевый (orange),
#ffff00 – желтый (yellow),
#00ff00 – зеленый (green),
#007dff – голубой (lightblue),
#0000ff – синий (blue),
#7d00ff – фиолетовый (purple).

Добавьте событие вызова функции при нажатия красной кнопки. Функция выводит в консоль текст: название red и код цвета #ff0000.

Измените функцию так, чтобы при нажатии на кнопку, менялся текст и цвет текста ранее созданной метки на соответствующее название цвета нажатой кнопки.

доработайте функцию так, чтобы при нажатии на кнопку, менялся текст и фон, ранее созданного, текстового поля на соответствующий код цвета нажатой кнопки:

"""


from tkinter import *
from tkmacosx import Button #https://pypi.org/project/tkmacosx/, Tkmacosx is a Python library extension to the Tkinter module that let you change background color of the button on macOS.

# def click_button():
#     print("red",red_button["bg"])
def set_red():
    label_upper.config(text="red", fg="#ff0000")
    color_text.config(text="#ff0000",bg="#ff0000")
    color_text.delete(0, END)
    color_text.insert(0, "Red")
    color_text.config(bg="#ff0000")


def set_orange():
    label_upper.config(text="orange", fg="#ff7d00")
    color_text.config(text="#ff7d00",bg="#ff7d00")
    color_text.delete(0, END)
    color_text.insert(0, "Orange")
    color_text.config(bg="#ff7d00")


def set_yellow():
    label_upper.config(text="yellow", fg="#ffff00")
    color_text.config(text="#ffff00",bg="#ffff00")
    color_text.delete(0, END)
    color_text.insert(0, "Yellow")
    color_text.config(bg="#ffff00")


def set_green():
    label_upper.config(text="green", fg="#00ff00")
    color_text.config(text="#00ff00",bg="#00ff00")
    color_text.delete(0, END)
    color_text.insert(0, "Green")
    color_text.config(bg="#00ff00")

def set_lightblue():
    label_upper.config(text="lightblue", fg="#007dff")
    color_text.config(text="#007dff",bg="#007dff")
    color_text.delete(0, END)
    color_text.insert(0, "lightblue")
    color_text.config(bg="#007dff")

def set_blue():
    label_upper.config(text="blue", fg="#0000ff")
    color_text.config(text="#0000ff", bg="#0000ff")
    color_text.delete(0, END)
    color_text.insert(0, "Blue")
    color_text.config(bg="#0000ff")

def set_purple():
    label_upper.config(text="purple", fg="#7d00ff")
    color_text.delete(0,END)
    color_text.insert(0,"Purple")
    color_text.config(bg="#7d00ff")


root = Tk()
root.title('Colors')
label_upper = Label(root,text="Color name",font=("Arial Bold",20))
label_upper.pack()
# label_upper  = Entry(root, width=50)
# label_upper.pack()

message = StringVar()
message.set("Color name")
color_text = Entry(root, justify ="center",  textvariable=message)
color_text.pack()

red_button = Button(root, text="1",bg="#ff0000", command = set_red)
red_button.pack()
orange_button = Button(root, text="2", bg="#ff7d00", command = set_orange)
orange_button.pack()
yellow_button = Button(root, text="3", bg="#ffff00",command = set_yellow)
yellow_button.pack()
green_button = Button(root, text="4", bg="#00ff00", command = set_green)
green_button.pack()
lightblue_button = Button(root, text="5", bg="#007dff", command = set_lightblue)
lightblue_button.pack()
lightblue_button.pack()
blue_button = Button(root, text="6",bg = "#0000ff", command = set_blue)
blue_button.pack()
purple_button = Button(root, text="7", bg="#7d00ff", command = set_purple)
purple_button.pack()

root.mainloop()

