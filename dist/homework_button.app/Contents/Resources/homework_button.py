# from tkinter import *
# root = Tk()
# button_one = Button(root, text="OK")
# button_two = Button(root, text="NOT OK")
# button_one.pack()
# button_two.pack()
# root.mainloop()


# from tkinter import *
# root = Tk()
# button_one = Button(root, text="OK")
# button_two = Button(root, text="Are you sure?")
# button_three = Button(root, text="Maybe not")
# button_one.pack()
# button_two.pack()
# button_three.pack()
# root.mainloop()

# from PIL import Image
#
# # Open and convert the image to PPM format
# img_path = "/Users/tuzova/Downloads/icons8.png"
# output_ppm = "/Users/tuzova/Downloads/icons8.ppm"
#
# img = Image.open(img_path)
# img.save(output_ppm, format="PPM")  # Convert and save as PPM
#
# print("Image converted to PPM format:", output_ppm)


# import tkinter as tk
#
# root = tk.Tk()
#
# icon_img = tk.PhotoImage(file="/Users/tuzova/Downloads/icons8.ppm")
# root.iconphoto(True, icon_img)
#
# button_one = tk.Button(root, text="OK", underline=10, font="Arial 30")
# button_one.pack()
#
# button_two = tk.Button(root, text="NOT OK", underline=1)
# button_two.pack()
#
# root.mainloop()

# from PIL import Image
#
# img_path = "/Users/tuzova/Downloads/icons8.png"
# output_ico = "/Users/tuzova/Downloads/icons8.ico"
#
# img = Image.open(img_path)
# img.save(output_ico, format="ICO")  # Convert and save as ICO
#
# print("Image converted to ICO format:", output_ico)

# import tkinter as tk
#
# root = tk.Tk()
#
# # Use the converted ICO file
# root.wm_iconbitmap("/Users/tuzova/Downloads/icons8.ico")
#
# button_one = tk.Button(root, text="OK", underline=10, font="Arial 30")
# button_one.pack()
#
# button_two = tk.Button(root, text="NOT OK", underline=1)
# button_two.pack()
#
# root.mainloop()

# from PIL import Image
#
# img_path = "/Users/tuzova/Downloads/icons8.png"
# output_icns = "/Users/tuzova/Downloads/icons8.icns"
#
# img = Image.open(img_path)
# img.save(output_icns, format="ICNS")  # Convert and save as ICNS
#
# print("Image converted to ICNS format:", output_icns)


import tkinter as tk

root = tk.Tk()

# Use the newly converted ICNS file
root.wm_iconbitmap("/Users/tuzova/Downloads/icons8.icns")

button_one = tk.Button(root, text="OK", underline=10, font="Arial 30")
button_one.pack()

button_two = tk.Button(root, text="NOT OK", underline=1)
button_two.pack()

root.mainloop()




