 #Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print ("hello")
a = str (input ("введите число "))
sum = 0 
for  i in  a:
       if i.isdigit ():
        sum = sum + int (i)

print ("сумма цифр в числе равна ")
print (sum)


 
