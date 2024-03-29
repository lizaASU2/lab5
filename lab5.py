# Программисты предпочитают применять генераторы в тех случаях, когда нет необходимости сохранять всю последовательность
# и промежуточные значения в памяти
# Функция, которая обрабатывает большую последовательность и использует обычный return,
# требует от интерпретатора выделять ей много памяти.
# И если обычно такие функции не сильно влияют на производительность программы, то в проектах,
# содержащих последовательности с миллионами элементов, они потребляют очень много памяти.
# сдали лабу
# -----------------------часть, которую делала к чт.Просто иллистрирует работы yield-----------------------
from datetime import datetime


# функция, возвращающая список чисел от 0 до n с помощью return
def first(n):
    m = []
    for i in n:
        m.append(i)
    return m


# вывод списка
k = [1, 2, 3, 4, 5]
a = first(k)
print('return = ', a)


# функция, создает генератор чисел от 0 до n
def second(n):
    m = []
    for i in n:
        m.append(i)
        yield m  # yield создает генератор чисел


# Вывод генератора. Выводит <generator object second at 0x0296BDF0> т.к. не хранится в памяти
b = second(k)
print('yield 1= ', b)


# чтоб вернуть значения из генератора переберем их в цикле
for j in b:
    print('yield 2= ', j)

# чтоб вернуть текущее значение генератора
# print('next yield = ', next(b))

# ------------------------------норм часть--------------------------------------------------

n = [1, 2, 3, 4, 5]


#  квадрат числа
def g1(n):
    for i in n:
        yield i*i


# сумма
def g2(n):
    for i in n:
        yield i+i


# для проверки правильности работы программы
m = []
m1 = []

# сравниваем квадраты числа с его суммой и выводим наибольшее значение
print('-----результат сравнения --------')
for x, y in zip(g1(n), g2(n)):
    if x > y:
        print('x>y= ', x)
    else:
        print('y>x= ', y)
    if y not in m:
        m.append(y)
    m1.append(x)

print('-----исходные списки--------')
print('квадрат=', m1)
print('сумма =', m)


# считываем строки из двух файлов и записываем их в один список
def r1(file):
    with open(file) as f:
        for line in f:
            lst = line.split()
            yield lst


s = []
s1 = []
maxln = []
for x1, y1 in zip(r1('f1.txt'), r1('f2.txt')):
    s.append(x1)
    s1.append(y1)
    maxln.append(x1)
    maxln.append(y1)

print('-----исходные списки--------')
print('исходный файл 1=', s1)
print('исходный файл 2 =', s, '\n')
print('итоговый файл  =', maxln)
print("----------------------------")
f1 = open('1.txt', 'w')
f2 = open('2.txt', 'w')
N = 100000000  # при таком N функция func1 вызывает ошибку MemoryError, а func2 записывает данные в файл
# (при запуске закоммент 112 строчку) )


def func1(n):
    res = []
    for i in range(n):
        res.append(i**2)
    return res


t1 = datetime.now()
for i in func1(N):
    f1.write(str(i)+' ')
t2 = datetime.now()
print('Took {} seconds'.format(t2-t1))


def func2(n):
    for i in range(n):
        yield i**2  # Позднее продолжить работу с этого места


t1 = datetime.now()
for i in func2(N):  # Возобновить работу функции
    f2.write(str(i)+' ')
t2 = datetime.now()
print('Took {} seconds'.format(t2-t1))