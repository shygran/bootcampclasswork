#Создайте функцию которая генерирует 10 чисел Фибоначчи: 1,1,2,3,5,8,13,21,34,...


def fibo10(n):
   fib1 = fib2 = 1
   print(fib1, fib2)
   for i in range(2, n):
      fib1, fib2 = fib2, fib1 + fib2
      print(fib2)

fibo10(10)
