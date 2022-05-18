#Вам дан список имён names, вытащите 4 рандомных имени оттуда и сохраните в другой список.

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

import random

names2 = []

i = random.choice(names)
f = random.choice(names)
g = random.choice(names)
d = random.choice(names)

names2.append(i)
names2.append(f)
names2.append(g)
names2.append(d)

print(names2)

