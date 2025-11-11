width = 55
text = 'Содержание'
# print (f"{width_1.center(70)}")
print(text.center(width))
print('-'*width)

text = 'Шилов Александр. Вниз по Волге'
page = 3
print(f"{text.ljust(width-3, '.')}{str(page).rjust(3)}")

text = 'Шилов Д. Вниз по Волге'
page = 34
print(f"{text.ljust(width-3, '.')}{str(page).rjust(3)}")

text = 'Шилов И. Вниз по Волге'
page = 341
print(f"{text.ljust(width-3, '.')}{str(page).rjust(3)}")

width_2 = 'Пояркова Анастасия. Таежными тропами'
page = '24'
print(f"{width_2.ljust(70, '.')} {page.rjust(2)}")

width_4 = 'Кудимов Лев. Далеко в степи'
page = '54'
print (f"{width_4.ljust(70, '.')} {page.rjust(1)}")

width_5 = 'Дроздовский Виктор. Лесная избушка'
page = '81'
print (f"{width_5.ljust(70, '.')} {page.rjust(2)}")

width_6 = 'Борюсов Николай. Записки путешественника'
page = '126'
print (f"{width_6.ljust(70, '.')} {page.ljust(2)}")

width_7 = 'Коршунов Никита. Под сенью дуба'
page = '251'
print (f"{width_7.ljust(70, '.')} {page.rjust(2)}")

width_8 = 'Семенова Ирина. Маленький веночек'
page = '251'
print (f"{width_8.ljust(70, '.')} {page.rjust(2)}")

width_9 = 'Немирова Галина. Первое слово'
page = '334'
print (f"{width_9.ljust(70, '.')} {page.rjust(2)}")

width_10 = 'Маховский Дмитрий. Путевой обходчик'
page = '392'
print (f"{width_10.ljust(70, '.')} {page.rjust(2)}")

width_11 = 'Тараскин Егор. Его величесто случай'
page = '458'
print (f"{width_11.ljust(70, '.')} {page.rjust(2)}")