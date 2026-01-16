# 1.Создайте программу с тремя кнопками: 1, 2, 3. Расположите сверху вниз столбиком: 1, 2, 3 с привязкой к верхнему краю окна. Разверните окно на весь экран и проверьте корректность отображения.
#
# from tkinter import*
#
# root = Tk()
# button_top = Button(root,text="Button 1")
# button_top.pack(side=TOP)
# button_middle= Button(root,text="Button 2")
# button_middle.pack(side=TOP)
# button_bottom= Button(root,text="Button 3")
# button_bottom.pack(side=TOP)
# root.mainloop()



# 2. Создайте программу с тремя кнопками: 1, 2, 3. Расположите сверху вниз столбиком: 3, 2, 1 с привязкой к нижнему краю окна. Разверните окно на весь экран и проверьте корректность отображения.
# from tkinter import*
#
# root = Tk()
# button_top = Button(root,text="Button 1")
# button_top.pack(side=BOTTOM)
# button_middle = Button(root,text="Button 2")
# button_middle.pack(side=BOTTOM)
# button_bottom = Button(root,text="Button 3")
# button_bottom.pack(side=BOTTOM)
# root.mainloop()



# 3.Создайте программу с тремя кнопками: 1, 2, 3. Расположите строчкой: 1, 2, 3 с привязкой к левому краю окна. Разверните окно на весь экран и проверьте корректность отображения.

# from tkinter import*
#
# root = Tk()
# button_top = Button(root,text="Button 1")
# button_top.pack(side=LEFT)
# button_middle= Button(root,text="Button 2")
# button_middle.pack(side=LEFT)
# button_bottom = Button(root,text="Button 3")
# button_bottom.pack(side=LEFT)
# root.mainloop()


# 4. Создайте программу с тремя кнопками: 1, 2, 3. Расположите строчкой: 3, 2, 1 с привязкой к правому краю окна. Разверните окно на весь экран и проверьте корректность отображения.

# from tkinter import*
#
# root = Tk()
# button_top = Button(root,text="Button 1")
# button_top.pack(side=RIGHT)
# button_middle = Button(root,text="Button 2")
# button_middle.pack(side=RIGHT)
# button_bottom = Button(root,text="Button 3")
# button_bottom.pack(side=RIGHT)
# root.mainloop()




# 1.Создайте программу с двумя кнопками растягиваемые по горизонтали, прикрепленными к верхней и нижней границам окна.

# from tkinter import*
#
# root = Tk()
# button_top = Button(width=1,text="up")
# button_top.pack(side=TOP, fill=X)
# button_bottom = Button(width=5,text="down")
# button_bottom.pack(side=BOTTOM, fill=X)
# root.mainloop()

# 2.Создайте программу с двумя кнопками растягиваемые по вертикали, прикрепленными к левой и правой границам окна.
#
# from tkinter import*
#
# root = Tk()
# left_button = Button(width=5)
# left_button.pack(side=LEFT, fill=Y)
# right_button = Button(width=5)
# right_button.pack(side=RIGHT, fill=Y)
# root.mainloop()


# # 3.Напишите программу с кнопкой растягивающейся на всё окно, независимо от размера окна.
# from tkinter import*
#
# root = Tk()
# big_button = Button(text="Click me")
# big_button.pack(fill = BOTH, expand=True)
# root.mainloop()



# 4.Создайте четыре программы с кнопкой, которая будет привязана к углу окна. И при увеличении размеров окна виджет продолжит оставаться в том же углу:

# в левом верхнем углу окна;
# в правом верхнем углу окна;
# в левом нижнем углу окна;
# в правом нижнем углу окна;

#
# from tkinter import*
#
# root = Tk()
# button_top_left = Button(width=5)
# button_top_left.pack(anchor='nw')
# root.mainloop()
#
# from tkinter import*
#
# root = Tk()
# button_top_right = Button(width=5)
# button_top_right.pack(anchor='ne')
# root.mainloop()
#
# from tkinter import*
#
# root = Tk()
# button_bottom_left = Button(width=5)
# button_bottom_left.pack(anchor='sw', side="bottom")
# root.mainloop()
#
# from tkinter import*
#
# root = Tk()
# button_bottom_right = Button(width=5)
# button_bottom_right.pack(anchor='se', side="bottom")
# root.mainloop()


# """
# 5.Создайте одну программу с четырьмя кнопками по углам окна.
# И при увеличении размеров окна виджет продолжит оставаться в тех же углах:
# в левом верхнем углу окна;
# в правом верхнем углу окна;
# в левом нижнем углу окна;
# в правом нижнем углу окна;
# """
#
# from tkinter import*
#
# root = Tk()
# button_top_left = Button(width=5,text="Up left")
# button_top_left.pack(anchor='w')
# button_top_right = Button(width=5, text ="Up right")
# button_top_right.pack(anchor='e')
# button_top_left = Button(width=5, text="Bottom left")
# button_top_left.pack(anchor='w', side="bottom")
# button_bottom_right = Button(width=5,text="Bottom right")
# button_bottom_right.pack(anchor='e', side="bottom")
# root.mainloop()

"""
6.Создайте программу с центральным расположением метки с
"текстом "Центр". При увеличении размеров окна виджет продолжит оставаться по центру: по горизонтали и вертикали."""

# from tkinter import *
#
# root = Tk()
# label = Label(bg="black", width=30, height=10, text="Центр")
# label.pack(expand=1)
# root.mainloop()

