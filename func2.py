#Создайте с помощью рекурсии функцию которая генерирует 10 чисел Фибоначчи:
#1,1,2,3,5,8,13,21,34,...

def recur_fibo(n):
    

 if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

recur_fibo(1)
