#Написать lambda которая принимает 3 параметра и умножает все параметры между собой.
#Функция должна вернуть строку: "Объём бассейна " и значение которое получилось.

u = lambda q, w, e : q*w*e
print(f"Объём бассейна:", u(3,3,3))