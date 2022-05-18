#Создайте функцию сложения, затем функцию вычитания двух чисел...
#Создайте 3-ю функцию которая вызывает первые 2 внутри себя.

def addition(a, b):
   n = a + b
   print(n)

addition(2, 3)

def substraction(e, f):
   p = e - f
   print(p)

substraction(10, 7)

def addsub():
   addition(6, 8)
   substraction(90, 60)

addsub()
