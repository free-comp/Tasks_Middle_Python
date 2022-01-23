# 23. Показать таблицу квадратов чисел от 1 до N

def square(x):
    return x ** 2

n = int(input('Введите, до какого значения необходимо вывести таблицу квадратов: '))
ind = 0
for i in range (1,n+1):
    print("%5d" % square(i), end = ' ')
    ind+=1
    if ind == 10:
        print ()
        ind = 0
print ()