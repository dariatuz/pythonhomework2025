# text = input("Please input text:")
# print(text) if text else print("Empty string")
#
# a = 14
# b = -3
# print(a) if a > b else print(b)

# text = input("Please input text:")
# print(text.upper()) if len(text)<8 else print(text)


export PATH="/opt/homebrew/opt/tcl-tk/bin:$PATH"
export LDFLAGS="-L/opt/homebrew/opt/tcl-tk/lib"
export CPPFLAGS="-I/opt/homebrew/opt/tcl-tk/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/tcl-tk/lib/pkgconfig"python3 -c "print('ok')"


# #Определение чётности числа. Определите, чётное ли число x. Присвойте переменной result значение "even" или "odd".
result = input("Please input number: ")
evenodd = "odd" if int(result) % 2 else "even"
print(evenodd)

print("odd" if int( input("Please input number: ")) % 2 else "even")


#Применение скидки к товару. Если стоимость товара price выше 500, примените скидку в размере 20%. В противном случае — скидка 5%.
# price = input("Please input price")
#
# price = int(price)*(1-20/100) if int(price) > 500 else int(price)*(1-5/100)
#
# print(price)

# if int(price) > 500:
#     price = int(price)*(1-20/100)
# else:
#     price = int(price)*(1-5/100)