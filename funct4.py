#Создайте функцию которая принимает слово и создаёт файл с таким именем в той же директории, где был запущен Ваш .py файл.

filename = input("Впишите слово: ")

def filecreation(filename):
   open(filename, 'w')

filecreation(filename)
