



#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

#Пример:

    #пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int (input())
a = []
for i in range (n ):
  a.append (i*i+1)
print (a)
    
    