#Создайте файл users.txt. Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.

login = input("Введите логин: ")
password = input("Введите пароль: ")

with open('users.txt', 'a') as f:
   f.write(f'{login} : {password}')
