 #Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
#округлённую до трёх знаков после точки.
n = int (input("Введите число "))
a = []
for i in range (n+1):
  a.append ((1+1/n)**n)
b = sum (a,1) 
c = round((b),2)
print (c)
 
