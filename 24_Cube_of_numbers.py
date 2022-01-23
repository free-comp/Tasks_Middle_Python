# 24. Найти кубы чисел от 1 до N

def cube(x):
    return pow(x,3)

n = int(input('Введите N: '))

print(f'Кубы чисел от 1 до {n}:')
for i in range(1, n+1):
    print(cube(i), end = ' ')
print()