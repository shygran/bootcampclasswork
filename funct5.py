#Создайте 2 функции где одна функция вложена в другую.
#Главная функция должна выводить на экран текст: "Я главная функция". 
#А вложенная функция должна выводить на экран: "Я вложенная функция."

def func1(a):
   def func2():
      print(f"{a}\nЯ вложенная функция")
   func2()

func1("Я главная функция")
