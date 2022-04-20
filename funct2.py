#Напишите функцию которая принимает 2 Dictionary и добавляет втрорую Dictionary к первой.

def addition(a, b):
   a.update(b)
   return a

print(addition({'fly': 0, 'pr': 1}, {'k': 3, 'fl': 5}))


