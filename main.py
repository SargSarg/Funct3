def fact(n):
    if n == 1: #терминальный случай который остановит рекурсивные вызовы
        return 1
    return n * fact(n-1) #рекурсивный вызов
c = fact(3)
print(c)

def rec_fibb(n):
   if n == 1:
       return 1
   if n == 2:
      return 1
   return rec_fibb(n - 1) + rec_fibb(n - 2)

c = rec_fibb(10)  # 55
print(c)

def rec_sum(n): #найти сумму чисел от 1 до n
   if n == 1:  # терминальный случай
       return 1
   return n + rec_sum(n - 1)  # рекурсивный вызов
c = rec_sum(4)  # 55
print(c)

def reverse_str(string): #развернуть строку
   if len(string) == 0:
       return ''
   else:
       return string[-1] + reverse_str(string[:-1])
z = reverse_str('test')  # tset
print(z)

def sum_digit(n): #вычислить сумму цифр числа
   if n < 10:
       return n
   else:
       return n % 10 + sum_digit(n // 10)
b = sum_digit(123)  # 6
print(b)