# line = 'some STRING. AnY STRING.'
# print(f'{line.rjust(50) = }')
#
# line = '\t1\t22\t333\t4444\t5'
# print(f'{line  }')
# line = '0\t11\t2222\t3333333\t44444444\t5'
# print(f'{line }')
# line = '\t1\t22\t333\t4444\t5'
# print(f'{line.expandtabs()  }')
# line = '0\t11\t2222\t3333333\t44444444\t5'
# print(f'{line.expandtabs() }')
# line = '\t1\t22\t333\t4444\t5'
# print(f'{line.expandtabs(10)  }')
# line = '0\t11\t2222\t3333333\t44444444\t5'
# print(f'{line.expandtabs(-2) }')
# print(f'{line.expandtabs(0) }')
# print(f'{line.expandtabs(1) }')
# print(f'{line.expandtabs(2) }')

line = ' ometext anytext '
print(line)
print(line.replace('s','S'))
print(line.replace('text',' text'))
print(line.replace('text',' text',1))
print(line.replace('text',' text').replace('s','S'))
print(line)
print(line.replace(' ',"_"))
