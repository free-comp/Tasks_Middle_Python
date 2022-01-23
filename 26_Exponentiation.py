# 26. Возведите число А в натуральную степень B используя цикл.

def power(a,n):
    res = 1
    for i in range(n): 
        res*= a  # res=res*a
    return res
   

a = int(input('Введите число: '))
b = int(input('Введите степень числа: '))

print(f'Число {a} в степени {b}:', power(a,b))