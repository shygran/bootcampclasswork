#Напишите программу которая выводит только нечётные числа с помощью рекурсии.

#def rec(a):
#   if a%2 == 0:
#      return(rec(a+1))
#   elif a%2 != 0:
#      return(rec(a+2)

#print(rec(5))

def rec(a):
    print(a)
    rec(a+2)
rec(1)
