# Спросите у пользователя имя файла. Создайте функцию которая создаёт файл с именем которое передал пользователь. Присвойте ИМЯ функции к переменной и вызывайте функцию через переменную.

a = input("Введите имя файла: ")

def file_creation(a):
   f = open(a, w)
   print(f)

