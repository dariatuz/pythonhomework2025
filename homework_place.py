"""1.Создайте окно заданного размера: 400 на 400 пикселей. Для решения используйте метод place() и абсолютное позиционирование x, y:

добавьте в четыре кнопки по углам, названия кнопок должны соответствовать их месту положения;
добавьте ещё одну кнопку расположенную по центру окна;
измените размер окна мышкой, и проанализируйте результат работы интерфейса.
"""

# from tkinter import*
#
# root =Tk()
# root.geometry("400x400")
#
# button_top_left = Button(text="top left", font=13)
# button_top_left.place(relx=0, rely=.0, anchor='n')
# button_top_right = Button(text="top right", font=13)
# button_top_right.place(relx=.78, rely=.0)
# button_bottom_left = Button(text="bottom left", font=13)
# button_bottom_left.place(relx=0, rely=.93)
# button_bottom_right = Button(text="bottom right", font=13,  anchor='sw')
# button_bottom_right.place(relx=.8, rely=.93)
# button_center = Button(text="center", font=13, anchor='w')
# button_center.place(relx=.5, rely=.5, anchor="c")
#
# root.mainloop()


"""2.Создайте окно заданного размера: 600 на 300 пикселей. Для решения используйте метод place() и относительное позиционирование relx, rely:

добавьте в четыре кнопки по центру сторон, названия кнопок должны соответствовать их месту положения;
добавьте ещё одну кнопку расположенную по центру окна;
измените размер окна мышкой, и проанализируйте результат работы интерфейса.
"""

# from tkinter import*
#
# root =Tk()
# root.geometry("400x400")
#
# button_top = Button(text="top", font=13)
# button_top.place(relx=.5, rely=0, anchor="n")
# button_left = Button(text="left", font=13)
# button_left.place(relx=0, rely=.5, anchor="w")
# button_right = Button(text="right", font=13)
# button_right.place(relx=.99, rely=.5, anchor="e")
# button_bottom = Button(text="bottom", font=13,  anchor='sw')
# button_bottom.place(relx=.5, rely=.99, anchor="s")
# button_center = Button(text="center", font=13, anchor='w')
# button_center.place(relx=.5, rely=.5, anchor="center")
#
# root.mainloop()

"""3.Создайте окно заданного размера: 200 на 100 пикселей. 
Для решения используйте метод place() и относительное позиционирование relx, rely, anchor:

при одном нажатии на кнопку, она должна перемещаться 
по часовой стрелке на одну позицию: с верху на право, 
затем вниз, затем налево и обратно наверх.
при изменении размера окна положение кнопки 
должно корректно отображаться по краям окна."""


from tkinter import *

clicks = 0


def move_button():
    global clicks
    clicks = (clicks + 1) % 4
    if clicks == 0:
        button_top.place(relx=.5, rely=0, anchor="n")
        button_top.config(text="Top")
    elif clicks == 1:
        button_top.place(relx=.99, rely=.5, anchor="e")
        button_top.config(text="Right")
        button_top.pack_forget()
    elif clicks == 2:
        button_top.place(relx=.5, rely=.99, anchor="s")
        button_top.config(text="Bottom")
    elif clicks == 3:
        button_top.place(relx=0, rely=.5, anchor="w")
        button_top.config(text="Left")

    # elif clicks == 3:
    # button_top.place(relx=0, rely=.5, anchor="w")
    # button_top.config(command=move_button, text="Left")
    # elif clicks == 4:
    # button_top.place(relx=0, rely=.5, anchor="w")
    # button_top.config(command=move_button, text="Left")

root = Tk()
root.geometry("200x100")

button_top = StringVar()
button_top = Button(text="Top", font=13, command=move_button)
button_top.place(relx=.5, rely=0, anchor="n")
button_top.pack()
# button_right = Button(text="right", font=13)
# button_right.place(relx=.99, rely=.5, anchor="e")
# button_bottom = Button(text="bottom", font=13,  anchor='sw')
# button_bottom.place(relx=.5, rely=.99, anchor="s")
# button_left = Button(text="left", font=13)
# button_left.place(relx=0, rely=.5, anchor="w")

root.mainloop()





