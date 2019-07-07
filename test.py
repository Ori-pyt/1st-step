'''
i = 3
print(i)
print(i & 2)
s = """Это многострочная строка.
Это вторая её строчка."""
print(s)
'''

# Calculator with two variables
number_1 = int(input('Enter your number(a): '))
number_2 = int(input('Enter your number(b): '))
print('What do you wanna do with this numbers?( p-plus | m-minus | mul-multiplication | d-division )')
action = str(input('Enter your number: '))
if action == 'p':
    print('a + b='+str(number_1 + number_2))
elif action == 'm':
    print('a - b='+str(number_1 - number_2))
elif action == 'mul':
    print('a * b='+str(number_1 * number_2))
elif action == 'd':
    print('a / b='+str(number_1 / number_2))
else:
    print('No such action')

print('end')