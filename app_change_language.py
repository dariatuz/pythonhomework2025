"""Напишите программу-форму с переключением интерфейса английский/русский."""

from tkinter import*


def change_language():
    text = button_language_switch.cget("text")
    # print(text=="English")
    if text=="English":
        label_name.config(text="Имя пользователя")
        label_user_surname.config(text="Фамилия пользователя")
        label_user_birth_year.config(text="Год рождения пользователя")
        button_language_switch.config(text="Русский")
    else:
        label_name.config(text="User name")
        label_user_surname.config(text="User Surname")
        label_user_birth_year.config(text="Birth year")
        button_language_switch.config(text="English")

root = Tk()
root.geometry("400x200")

label_name = Label(root, text="User name",)
label_name.place(x=20, y=20)

text_field_upper = Entry(root, width=20, bg="white", fg="black",)
text_field_upper.place(x=140, y=20)

label_user_surname = Label(root, text="User surname")
label_user_surname.place(x=20, y=60)

text_field_middle = Entry(root, width=20, bg="white", fg="black")
text_field_middle.place(x=140, y=60)

label_user_birth_year = Label(root, text="User birth year")
label_user_birth_year.place(x=20, y=100)

text_field_bottom = Entry(root, width=20, bg="white", fg="black")
text_field_bottom.place(x=140, y=100)

button_language_switch = Button(text="English", font=13, command=change_language)
button_language_switch.place(x=140, y=150, anchor="w")

root.mainloop()