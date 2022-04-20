#Допустим у нас есть список языков программирования. lang1 = 'Rust'
#languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
#Обязательное условие: если переменная в списке, то нужно вывести на экран 'this languages is in list'. 
#Если этого языка нет в списке, ничего не нужно выводить.

lang1 = 'Rust'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']

while lang1 in languages:
	print("this language is in the list")
	break
