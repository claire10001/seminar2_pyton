#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на позициях a и b.
#Значения N, a и b вводит пользователь с клавиатуры.

#x = int (input ("введите число "))
#y = int (input ("введите число "))
n = int (input("введите число "))
a = []
for i in range (n):
 print (-i,i)
b = int (input("введите номер первого элемента "))
c = int (input("введите номер второго элемента "))
a.append ((i + b)*(i + c))
print (a) 
  