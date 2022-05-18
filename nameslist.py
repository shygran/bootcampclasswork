#Возьмите список имён из задания №2 и сформируйте 4 разные команды из всех участников.

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]
(len(names))

import random

random.shuffle(names)

team1 = names[0:4]
team2 = names[4:7]
team3 = names[7:10]
team4 = names[10:14]
print(team1, team2, team3, team4)
