#Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”,
#то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”. Подсказка: используйте ключевое слово in.

with open('users.txt', 'r') as f:
   if 'w' in f.read() or 'W' in f.read():
      print('Да, в тексте есть w')
   else:
      print('нет')