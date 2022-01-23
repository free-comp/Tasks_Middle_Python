# 25. Найти сумму чисел от 1 до А

def sum(numb):
    result = 0
    for numb in numb:
        result = result + numb
    return result

a = int(input('Введите целое положительное число: '))
ran = range(1, a+1)
print(f'Сумма чисел от 1 до {a}: ', sum(ran))



# через sum:
# ran = range(1, a+1)
# print(f'Сумма чисел от 1 до {a}: ', sum(ran))





