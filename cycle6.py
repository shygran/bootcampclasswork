#Если первое имя = 0, второе имя = 1 и т.д.
#Выведите на экран всё имена которые лежат на чётных числах

names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават','Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан',)
for i in range(1,len(names),2):
	print(names[i])