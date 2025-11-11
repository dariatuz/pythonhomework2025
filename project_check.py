width_1 = 'Секция: продукты питания'
print (f"{width_1.ljust(70)}")


product_name_1 = 'Одеяло 1.5 сп, файбер + бязь'
price = 699.00
numberofproducts = '1'
finalprice = 698.10
print(f"{product_name_1.ljust(3)} {price:>10.2f} {numberofproducts:>10} {finalprice:>10.2f}")


productname_2 = 'Подушка пух-перо 50x70 арт.1'
price = 299.00
numberofproducts = '2'
finalprice= 598.00
print(f"{productname_2.ljust(3)} {price:>10.2f} {numberofproducts:>10} {finalprice:>10.2f}")


productname_3 = 'Пакет ЛЕНТА майка'
price = 4.00
numberofproducts = '3'
finalprice = 8.00
print(f"{productname_3.ljust(3)}{price:>15.2f} {numberofproducts:>8} {finalprice:>8.2f}")


productname_4 = 'Нектар апельсин Неос'
price = 65.49
numberofproducts = '1'
finalprice = 65.49
print(f"{productname_4.ljust(3)} {price:>13.2f} {numberofproducts:>9.5} {finalprice:>9.2f}")


productname_5 = 'Итого:'
price_5 = 10000
print(f"{productname_5.ljust(3)} {price_5:>56.2f} ")



