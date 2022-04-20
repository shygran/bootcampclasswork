#Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
#С помощь цикла for пройти вывести на экран строку:
#"Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

name1 = input("Введите ваше имя: ")
prof1 = input("Ваша профессия: ")
name2 = input("Введите ваше имя: ")
prof2 = input("Ваша профессия: ")
name3 = input("Введите ваше имя: ")
prof3 = input("Ваша профессия: ")
name4 = input("Введите ваше имя: ")
prof4 = input("Ваша профессия: ")
name5 = input("Введите ваше имя: ")
prof5 = input("Ваша профессия: ")

thisdict = {}
thisdict[name1] = prof1
thisdict[name2] = prof2
thisdict[name3] = prof3
thisdict[name4] = prof4
thisdict[name5] = prof5

print(thisdict)

for key, value in thisdict.items():
	print("Здравствуйте!", f"Key: {key}")
	print("Прекрасная профессия", f"Value: {value}")
