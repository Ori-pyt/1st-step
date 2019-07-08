'''
i = 3
print(i)
print(i & 2)
s = """Это многострочная строка.
Это вторая её строчка."""
print(s)
'''

# Calculator with two variables
'''number_1 = int(input('Enter your number(a): '))
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

print('end')'''


# Area of ​​a right triangle
'''h = int(input('High:'))
b = int(input('Base:'))
a = 1/2*(h*b)
print('Area = ', a)

n = int(input('School:'))
k = int(input('Apple:'))
if n > k:
    print(k/n)
elif k >n:
    print('for schoolchildren ', k//n)
    print('apples in the basket ', k%n)
else:
    print(1)'''

# While
'''
number = 23
running = True
while running:
    guess = int(input('Введите целое число : '))
    if guess == number:
        print('Поздравляю, вы угадали.')
        running = False # это останавливает цикл while
    elif guess < number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого.')
else:
    print('Цикл while закончен.')
# Здесь можете выполнить всё что вам ещё нужно
print('Завершение.')'''

# Chess board
'''
print('Координаты первой клетки:')
a1 = int(input())
a2 = int(input())
print('Координаты второй клетки:')
b1 = int(input())
b2 = int(input())
if ((a1+a2)%2 == 0 and (b1+b2)%2 == 0) or ((a1+a2)%2 != 0 and (b1+b2)%2 != 0):
    print('YES')
else:
    print('NO')
print('end')'''
'''
m = int(input('Борт1 '))
n = int(input('Борт2 '))
x = int(input('Расстояние от более длинного борта:')) # Расстояние от более длинного борта
y = int(input('Расстояние от более короткого борта:')) # Расстояние от более короткой
if m > n :
    x1 = n - x
    y1 = m - y
else:
    x1 = m - x
    y1 = n - y
    
if x1 < x:
    m = x1
else:
    m = x
if y1 < y:
    n = y1
else:
    n = y
if n < m:
    print(n)
else:
    print(m)'''


# For, while
a = int(input())
b = int(input())
for i in range(a - (a + 1) % 2, b - b % 2, -2):
    print(i, end=' ')