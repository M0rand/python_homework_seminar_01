# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

n = int(input("Введите номер билета: "))
a = 0
b = 0

while n >= 1000:
    a += n % 10
    n = n // 10
while n:
    b += n % 10
    n = n // 10
print(a, b)        
if a != b:    
    print("no")
elif a == b:
    print("yes")