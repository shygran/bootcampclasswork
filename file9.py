#Создайте текстовый файл с целыми числами ->Найти максимальное и минимальное число и записать в другой файл.

with open('числа.txt', 'w') as f:
   f.write('10, 5, 50, 101, 300, 1730, 1819, 4000, 90300, 2')

with open('числа.txt', 'r') as f:
   for num in f.readline().split(','):
      print(max(num))
